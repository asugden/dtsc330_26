import keras
import tensorflow as tf


class TokenAndPositionEmbedding(keras.layers.Layer):
    def __init__(self, vocab_size, maxlen, embed_dim):
        super().__init__()
        self.token_emb = keras.layers.Embedding(vocab_size, embed_dim)
        self.pos_emb = keras.layers.Embedding(maxlen, embed_dim)

    def call(self, x):
        length = tf.shape(x)[1]
        positions = tf.range(start=0, limit=length, delta=1)
        positions = self.pos_emb(positions)
        x = self.token_emb(x)
        return x + positions
