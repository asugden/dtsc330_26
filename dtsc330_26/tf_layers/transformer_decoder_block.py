import keras
import tensorflow as tf


class TransformerDecoderBlock(keras.layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, dropout=0.1):
        super().__init__()
        self.self_attn = keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim
        )
        self.cross_attn = keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim
        )

        self.ffn = keras.Sequential(
            [
                keras.layers.Dense(ff_dim, activation="relu"),
                keras.layers.Dense(embed_dim),
            ]
        )

        self.norm1 = keras.layers.LayerNormalization()
        self.norm2 = keras.layers.LayerNormalization()
        self.norm3 = keras.layers.LayerNormalization()

        self.drop1 = keras.layers.Dropout(dropout)
        self.drop2 = keras.layers.Dropout(dropout)
        self.drop3 = keras.layers.Dropout(dropout)

    def call(self, x, enc_out, training=False, enc_mask=None):
        self_attn_out = self.self_attn(x, x, use_causal_mask=True)
        self_attn_out = self.drop1(self_attn_out, training=training)
        x = self.norm1(x + self_attn_out)

        cross_attn_out = self.cross_attn(x, enc_out, attention_mask=enc_mask)
        cross_attn_out = self.drop2(cross_attn_out, training=training)
        x = self.norm2(x + cross_attn_out)

        ffn_out = self.ffn(x)
        ffn_out = self.drop3(ffn_out, training=training)
        return self.norm3(x + ffn_out)
