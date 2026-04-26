import keras

from dtsc330_26.tf_layers import (
    token_position_embedding,
    transformer_decoder_block,
    transformer_encoder_block,
)


def build_model(vocab_size, maxlen=32, embed_dim=64, num_heads=2, ff_dim=128):
    enc_inputs = keras.Input(shape=(None,), dtype="int32", name="encoder_input")
    dec_inputs = keras.Input(shape=(None,), dtype="int32", name="decoder_input")

    enc_x = token_position_embedding.TokenAndPositionEmbedding(
        vocab_size, maxlen, embed_dim
    )(enc_inputs)
    enc_x = transformer_encoder_block.TransformerEncoderBlock(
        embed_dim, num_heads, ff_dim
    )(enc_x)

    dec_x = token_position_embedding.TokenAndPositionEmbedding(
        vocab_size, maxlen, embed_dim
    )(dec_inputs)
    dec_x = transformer_decoder_block.TransformerDecoderBlock(
        embed_dim, num_heads, ff_dim
    )(dec_x, enc_x)

    outputs = keras.layers.Dense(vocab_size, activation="softmax")(dec_x)

    return keras.Model([enc_inputs, dec_inputs], outputs)


if __name__ == "__main__":
    import numpy as np

    max_len = 20
    # Example data
    pairs = [
        ("recieve", "receive"),
        ("definately", "definitely"),
        ("wierd", "weird"),
        ("adres", "address"),
        ("acommodate", "accommodate"),
        ("seperate", "separate"),
        ("untill", "until"),
        ("goverment", "government"),
    ]

    # Vocabulary
    special_tokens = ["<pad>", "<bos>", "<eos>"]  # beginning of string, end of string
    chars = sorted(set("".join(x for p in pairs for x in p[0] + p[1])))
    vocab = special_tokens + chars

    token_to_id = {ch: i for i, ch in enumerate(vocab)}
    id_to_token = {i: ch for ch, i in token_to_id.items()}

    PAD = token_to_id["<pad>"]
    BOS = token_to_id["<bos>"]
    EOS = token_to_id["<eos>"]
    VOCAB_SIZE = len(vocab)

    max_src_len = max_len + 1  # (eos)
    max_target_len = max_len + 2  # (bos, eos)

    def encode_src(text):
        ids = [token_to_id[c] for c in text] + [EOS]
        ids += [PAD] * (max_src_len - len(ids))
        return ids

    def encode_target(text):
        # decoder input gets BOS + text
        dec_in = [BOS] + [token_to_id[c] for c in text]
        dec_in += [PAD] * (max_target_len - len(dec_in))

        # decoder target gets text + EOS
        dec_out = [token_to_id[c] for c in text] + [EOS]
        dec_out += [PAD] * (max_target_len - len(dec_out))
        return dec_in, dec_out

    src_data = []
    dec_in_data = []
    dec_out_data = []

    for src, tgt in pairs:
        s = encode_src(src)
        di, do = encode_target(tgt)
        src_data.append(s)
        dec_in_data.append(di)
        dec_out_data.append(do)

    src_data = np.array(src_data, dtype=np.int32)
    dec_in_data = np.array(dec_in_data, dtype=np.int32)
    dec_out_data = np.array(dec_out_data, dtype=np.int32)

    # sample weights so PAD tokens do not count in the loss
    sample_weights = (dec_out_data != PAD).astype(np.float32)

    # Build the model
    model = build_model(
        VOCAB_SIZE, maxlen=max_target_len, embed_dim=64, num_heads=2, ff_dim=128
    )

    model.compile(
        optimizer="adam",
        loss=keras.losses.SparseCategoricalCrossentropy(),
        metrics=["accuracy"],
    )

    model.fit(
        x=(src_data, dec_in_data),
        y=dec_out_data,
        sample_weight=sample_weights,
        epochs=300,
        verbose=1,
    )

    # --- Inference: correct a misspelled word ---
    def correct(word):
        """Feed a misspelled word through the model and decode the output."""
        src = np.array([encode_src(word)], dtype=np.int32)

        # Start the decoder with just <bos>
        decoded = [BOS]
        for _ in range(max_target_len - 1):
            dec = np.array(
                [decoded + [PAD] * (max_target_len - len(decoded))], dtype=np.int32
            )
            preds = model.predict([src, dec], verbose=0)
            next_id = int(np.argmax(preds[0, len(decoded) - 1]))
            if next_id == EOS:
                break
            decoded.append(next_id)

        return "".join(id_to_token[i] for i in decoded[1:])  # skip <bos>

    # Test on training examples
    print("\n--- Spell correction results ---")
    for wrong, right in pairs:
        result = correct(wrong)
        status = "ok" if result == right else "WRONG"
        print(f"  {wrong:15s} -> {result:15s}  (expected: {right}) [{status}]")
