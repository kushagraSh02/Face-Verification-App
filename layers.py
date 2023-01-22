import tensorflow as tf
from tensorflow.keras.layers import Layer

class L1Dist(Layer):
    def __int__(self, **kwargs):
        super().__int__()

    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)