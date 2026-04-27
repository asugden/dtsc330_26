import json
import pathlib

import keras
import numpy as np
import wordfreq

from dtsc330_26.tf_layers import (
    token_position_embedding,
    tokenization,
    transformer_decoder_block,
    transformer_encoder_block,
)


class Seq2SeqTransformer:
    def __init__(
        self,
        max_len: int = 32,
        embed_dim: int = 64,
        num_heads: int = 2,
        ff_dim: int = 128,
    ):
        """Initialize a seq2seq misspelling fixing transformer.

        Args:
            max_len (int, optional): the maximum input string length.
                Defaults to 32.
            embed_dim (int, optional): the number of embedding dimensions.
                Defaults to 64. This is probably too high, but it is
                reasonable.
            num_heads (int, optional): the number of parallel attention
                blocks to run. Defaults to 2.
            ff_dim (int, optional): the number of dimensions in the
                feedforward layers in each transformer block. Defaults
                to 128.
        """
        vocab_size = len(tokenization.vocab())
        self._config = {
            "max_len": max_len,
            "embed_dim": embed_dim,
            "num_heads": num_heads,
            "ff_dim": ff_dim,
        }
        self.tokenizer = tokenization.Tokenization(max_len=max_len)
        self.model = self._create_model(
            vocab_size, max_len, embed_dim, num_heads, ff_dim
        )
        # Categorical crossentropy computes the loss AFTER softmax
        # between the predicted probability of the true label and
        # the value of 1.0
        # loss = -log(pred[correct_class])

        # Sparse categorical cross entropy is the same on tokenized
        # output rather than one-hot encoded.

        # Label smoothing is valuable here. It doesn't allow
        # probabilities of 0 or 1, instead pushing them to 0.1 or 0.9
        # Label smooothing improves generalization.
        #
        # Pad tokens are ignored automatically because the embedding layer
        # uses mask_zero=True, which propagates a mask through the model.
        vocab_size = len(tokenization.vocab())

        def smoothed_sparse_xent(y_true, y_pred):
            smoothing = 0.1
            y_onehot = keras.ops.one_hot(keras.ops.cast(y_true, "int32"), vocab_size)
            y_smooth = y_onehot * (1.0 - smoothing) + smoothing / vocab_size
            return keras.losses.categorical_crossentropy(y_smooth, y_pred)

        self.model.compile(
            optimizer="adam",
            loss=smoothed_sparse_xent,
            metrics=["accuracy"],
        )

    def fit(
        self, wrong_correct_pairs: list[tuple[str, str]], training_epochs: int = 50
    ):
        """Fit a model from a list of pairs of wrong and correct words."""
        wrong_data, corrected_comparison_data, corrected_label_data = (
            self._word_pairs_to_matrix(wrong_correct_pairs)
        )
        # Pad tokens are automatically ignored during training because the
        # embedding layer uses mask_zero=True, which propagates a mask
        # through the model and suppresses pad positions in the loss.
        self.model.fit(
            x=(wrong_data, corrected_comparison_data),
            y=corrected_label_data,
            epochs=training_epochs,
            verbose=1,
            batch_size=128,
            shuffle=True,
            validation_split=0.05,
        )

    def correct(self, txt: str, beam_width: int = 4, freq_weight: float = 1.0) -> str:
        """Fix a misspelled word through the model using beam search decoding.

        Unlike greedy decoding (single_correct), beam search keeps the
        beam_width most promising partial sequences alive at each step rather
        than committing to the single best token. This lets it recover from
        a locally bad choice early in the word.

        After the full word is decoded, each candidate is also scored by
        how common that word is in English (via wordfreq), so real words
        like "forward" beat character-plausible non-words like "forrard".

        Args:
            txt: the misspelled input word.
            beam_width: how many candidate sequences to keep at each step.
            freq_weight: how strongly to prefer common English words.
                Higher values make the model more conservative (closer to
                a dictionary lookup). 0 disables the frequency prior.
                1 sets the model and frequency weights to be equal.
        """
        input_array = self.tokenizer.encode_input(txt)
        pad_len = self._config["max_len"] + 2

        # Each beam is a tuple of (cumulative_log_prob, token_id_list).
        # We start every beam from <bos>, with log-prob 0.
        # The term "beam" refers to beams of light in darkness
        beams: list[tuple[float, list[int]]] = [(0.0, [self.tokenizer.bos])]
        completed: list[tuple[float, list[int]]] = []

        for _ in range(self._config["max_len"] + 1):
            candidates: list[tuple[float, list[int]]] = []

            # Batch all beams into a single model call instead of one call per beam.
            enc_batch = np.tile(input_array[np.newaxis, :], (len(beams), 1))
            dec_batch = np.array(
                [
                    decoded + [self.tokenizer.pad] * (pad_len - len(decoded))
                    for _, decoded in beams
                ],
                dtype=np.int32,
            )
            # preds shape: (num_beams, seq_len, vocab_size)
            preds = self.model.predict([enc_batch, dec_batch], verbose=0)

            for i, (log_prob, decoded) in enumerate(beams):
                # We only care about the distribution at the last real position.
                next_token_probs = preds[i, len(decoded) - 1]

                # Expand each beam into beam_width new candidates by picking
                # the beam_width most probable next tokens.
                top_ids = np.argsort(next_token_probs)[-beam_width:]
                for next_id in top_ids:
                    new_log_prob = log_prob + np.log(next_token_probs[next_id] + 1e-10)
                    new_decoded = decoded + [int(next_id)]

                    if int(next_id) == self.tokenizer.eos:
                        completed.append((new_log_prob, new_decoded))
                    else:
                        candidates.append((new_log_prob, new_decoded))

            if not candidates:
                break

            # Keep only the beam_width best partial sequences for the next step.
            beams = sorted(candidates, key=lambda x: x[0], reverse=True)[:beam_width]

        # If nothing ever produced <eos>, treat the current beams as completed.
        if not completed:
            completed = beams

        # Re-rank completed sequences by combining the model log-prob with
        # the log word-frequency.  freq_weight controls the trade-off.
        def final_score(log_prob: float, decoded: list[int]) -> float:
            word = self.tokenizer.decode(decoded)
            freq = wordfreq.word_frequency(word, "en")
            # word_frequency returns 0 for unknown words; clamp to avoid log(0)
            freq = max(freq, 1e-10)
            return log_prob + freq_weight * np.log(freq)

        best = max(completed, key=lambda x: final_score(x[0], x[1]))
        return self.tokenizer.decode(best[1])

    def single_correct(self, txt: str) -> str:
        """Feed a misspelled word through the model and decode the output."""
        input_array = self.tokenizer.encode_input(txt)

        # Start the decoder with a beginning of string. We will add onto
        # it exactly as LLMs append tokens onto strings.
        decoded = [self.tokenizer.bos]

        # The decoder can produce + 2 length (<bos> and <eos>). We
        # already have bos, so we can loop through + 1
        for _ in range(self._config["max_len"] + 1):
            # The decoder still has to be of the correct length
            decoded_array = np.array(
                decoded
                + [self.tokenizer.pad] * (self._config["max_len"] + 2 - len(decoded)),
                dtype=np.int32,
            )
            preds = self.model.predict(
                [input_array[np.newaxis, :], decoded_array[np.newaxis, :]], verbose=0
            )

            # Find the last predicted value and check for end of string
            next_id = int(np.argmax(preds[0, len(decoded) - 1]))
            if next_id == self.tokenizer.eos:
                break

            decoded.append(next_id)

        return self.tokenizer.decode(decoded)

    def save(self, path: str):
        """Save model weights and hyperparameters to disk.

        Writes two files:
          <path>.weights.h5  — Keras weight file
          <path>.json        — hyperparameters needed to reconstruct the model
        """
        p = pathlib.Path(path)
        self.model.save_weights(str(p.with_suffix(".weights.h5")))
        p.with_suffix(".json").write_text(json.dumps(self._config))

    def load(self, path: str):
        """Load a previously saved Seq2SeqTransformer from disk.

        Args:
            path: the same base path passed to save() (without extension).
        """
        p = pathlib.Path(path)
        config = json.loads(p.with_suffix(".json").read_text())
        self.__init__(**config)
        self.model.load_weights(str(p.with_suffix(".weights.h5")))

    def _word_pairs_to_matrix(
        self, wrong_correct_pairs: list[tuple[str, str]]
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Convert word pairs to three numpy matrices of input training,
        decoder input (for comparison), and decoder output (for label)."""
        wrong_data = []
        corrected_comparison_data = []
        corrected_label_data = []

        for src, tgt in wrong_correct_pairs:
            s = self.tokenizer.encode_input(src)
            di, do = self.tokenizer.encode_label(tgt)
            wrong_data.append(s)
            corrected_comparison_data.append(di)
            corrected_label_data.append(do)

        wrong_data = np.array(wrong_data, dtype=np.int32)
        corrected_comparison_data = np.array(corrected_comparison_data, dtype=np.int32)
        corrected_label_data = np.array(corrected_label_data, dtype=np.int32)

        return wrong_data, corrected_comparison_data, corrected_label_data

    def _create_model(
        self,
        vocab_size: int,
        max_len: int = 32,
        embed_dim: int = 64,
        num_heads: int = 2,
        ff_dim: int = 128,
    ):
        """Create the model itself."""
        enc_inputs = keras.Input(shape=(None,), dtype="int32", name="encoder_input")
        dec_inputs = keras.Input(shape=(None,), dtype="int32", name="decoder_input")

        enc_x = token_position_embedding.TokenAndPositionEmbedding(
            vocab_size, max_len + 1, embed_dim
        )(enc_inputs)

        # Have two encoders to improve performance
        for _ in range(2):
            enc_x = transformer_encoder_block.TransformerEncoderBlock(
                embed_dim, num_heads, ff_dim
            )(enc_x)

        dec_x = token_position_embedding.TokenAndPositionEmbedding(
            vocab_size, max_len + 2, embed_dim
        )(dec_inputs)

        for _ in range(2):
            dec_x = transformer_decoder_block.TransformerDecoderBlock(
                embed_dim, num_heads, ff_dim
            )(dec_x, enc_x)

        outputs = keras.layers.Dense(vocab_size, activation="softmax")(dec_x)

        return keras.Model([enc_inputs, dec_inputs], outputs)
