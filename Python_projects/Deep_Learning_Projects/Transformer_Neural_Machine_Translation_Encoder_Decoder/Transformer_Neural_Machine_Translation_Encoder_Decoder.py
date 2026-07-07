# ===============================================================================
# Project : Neural Machine Translation using Transformer (Encoder-Decoder)
# Author  : Aryan Pandharinath Dhumal
# Created : 2026-07-07

# Description:
# ------------
# This program demonstrates an end-to-end implementation of a Transformer-based
# Neural Machine Translation (NMT) model using TensorFlow/Keras.

# Workflow:
# 1. Dataset Creation
# 2. Text Vectorization
# 3. Token & Positional Embedding
# 4. Transformer Encoder
# 5. Transformer Decoder
# 6. Model Construction
# 7. Model Training
# 8. Vocabulary Mapping
# 9. Sentence Translation
# 10. Testing

# Framework:
# - TensorFlow 2.x
# - Keras Functional API

# ===============================================================================

# =============================================================================
# Required Libraries
# =============================================================================

import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

# ------------------------------------------------------------
# Utility Header
# ------------------------------------------------------------

def Header(step, title):
    # Display a formatted section header.

    # Parameters
    # ----------
        # step : int
        #     Current execution step number.

        # title : str
        #     Title of the current execution phase.

    # Returns :  None
    
    print("\n" + "=" * 75)
    print(f"Step {step}: {title}")
    print("=" * 75)


# ============================================================
# Step 1: Dataset Creation
# ============================================================

Header(1, "Dataset Creation")

print("Creating small English to Marathi translation dataset.")

english_sentences = [
    "i love ai",
    "i love python",
    "we learn transformer",
    "this course is good",
    "teacher explains well",
    "students are learning",
    "machine learning is interesting",
    "deep learning is powerful",
    "i like this session",
    "this class is helpful"
]

marathi_sentences = [
    "mala ai avadte",
    "mala python avadte",
    "apan transformer shikto",
    "ha course changla aahe",
    "teacher changle samjavtat",
    "students shikat aahet",
    "machine learning interesting aahe",
    "deep learning powerful aahe",
    "mala ha session avadto",
    "ha class helpful aahe"
]

# Decoder output requires start and end tokens
target_sentences = ["start " + sentence + " end" for sentence in marathi_sentences]

for eng, mar in zip(english_sentences, target_sentences):
    print(eng, " ---> ", mar)


# ============================================================
# Step 2: Text Vectorization
# ============================================================

Header(2, "Tokenization and Padding")

print("Explanation: Converting English and Marathi words into token numbers.")

vocab_size = 1000
sequence_length = 8

english_vectorizer = layers.TextVectorization(
    max_tokens=vocab_size,
    output_sequence_length=sequence_length
)

marathi_vectorizer = layers.TextVectorization(
    max_tokens=vocab_size,
    output_sequence_length=sequence_length + 1
)

english_vectorizer.adapt(english_sentences)
marathi_vectorizer.adapt(target_sentences)

encoder_input_data = english_vectorizer(english_sentences)
target_token_data = marathi_vectorizer(target_sentences)

# Decoder input: start mala ai avadte
decoder_input_data = target_token_data[:, :-1]

# Decoder target: mala ai avadte end
decoder_target_data = target_token_data[:, 1:]

print("\nEnglish Vocabulary:")
for i, word in enumerate(english_vectorizer.get_vocabulary()):
    print(i, ":", word)

print("\nMarathi Vocabulary:")
for i, word in enumerate(marathi_vectorizer.get_vocabulary()):
    print(i, ":", word)

print("\nSample Encoder Input:")
print(english_sentences[0])
print(encoder_input_data[0].numpy())

print("\nSample Decoder Input:")
print(decoder_input_data[0].numpy())

print("\nSample Decoder Target:")
print(decoder_target_data[0].numpy())


# ============================================================
# Step 3: Positional Embedding Layer
# ============================================================

Header(3, "Token Embedding and Positional Embedding")

print("Transformer needs word meaning plus word position.")

class TokenAndPositionEmbedding(layers.Layer):
    """
    Custom Keras layer that combines token embeddings with
    positional embeddings.

    This enables the Transformer model to understand both
    word meaning and word order.

    Parameters
    ----------
    max_len : int
        Maximum sequence length.

    vocab_size : int
        Size of vocabulary.

    embed_dim : int
        Embedding vector dimension.
    """

    def __init__(self, max_len, vocab_size, embed_dim):
        """
        Initialize token and positional embedding layers.

        Parameters
        ----------
        max_len : int
            Maximum sequence length.

        vocab_size : int
            Number of unique words in vocabulary.

        embed_dim : int
            Embedding vector dimension.

        Returns
        -------
        None
        """
        super().__init__()

        self.token_embedding = layers.Embedding(
            input_dim=vocab_size,
            output_dim=embed_dim
        )

        self.position_embedding = layers.Embedding(
            input_dim=max_len,
            output_dim=embed_dim
        )

    def call(self, x):
        """
        Compute combined token and positional embeddings.

        This method generates token embeddings and positional embeddings,
        then performs element-wise addition to produce the final input
        representation for the Transformer.

        Parameters
        ----------
        x : Tensor
            Integer token IDs with shape
            (batch_size, sequence_length).

        Returns
        -------
        Tensor
            Combined embedding tensor of shape
            (batch_size, sequence_length, embed_dim).
        """
        length = tf.shape(x)[-1]

        positions = tf.range(start=0, limit=length, delta=1)

        token_embeddings = self.token_embedding(x)
        position_embeddings = self.position_embedding(positions)

        return token_embeddings + position_embeddings


# ============================================================
# Step 4: Transformer Encoder Block
# ============================================================

Header(4, "Transformer Encoder Block")

print("""
Encoder reads the complete English sentence.
It uses Multi-Head Self-Attention to understand relationships between words.
""")

class TransformerEncoder(layers.Layer):
    """
    Transformer Encoder block.

    The encoder processes the complete source sequence and generates
    contextual representations for every input token.

    Components:
    ----------
    • Multi-Head Self-Attention
    • Feed Forward Neural Network
    • Residual Connections
    • Layer Normalization
    • Dropout

    These components enable the encoder to capture long-range
    dependencies between words efficiently.

    Parameters
    ----------
    embed_dim : int
        Embedding dimension.

    num_heads : int
        Number of attention heads.

    ff_dim : int
        Hidden layer size of the feed-forward network.
    """

    def __init__(self, embed_dim, num_heads, ff_dim):
        """
        Initialize the Transformer Encoder.

        Parameters
        ----------
        embed_dim : int
            Size of embedding vectors.

        num_heads : int
            Number of attention heads.

        ff_dim : int
            Number of neurons in feed-forward network.

        Returns
        -------
        None
        """
        super().__init__()

        self.attention = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.ffn = tf.keras.Sequential([
            layers.Dense(ff_dim, activation="relu"),
            layers.Dense(embed_dim)
        ])

        self.layernorm1 = layers.LayerNormalization()
        self.layernorm2 = layers.LayerNormalization()

        self.dropout1 = layers.Dropout(0.1)
        self.dropout2 = layers.Dropout(0.1)

    def call(self, inputs, training=False):
        """
        Execute the forward pass of the encoder.

        Workflow
        --------
        1. Multi-Head Self-Attention
        2. Residual Connection
        3. Layer Normalization
        4. Feed Forward Network
        5. Residual Connection
        6. Layer Normalization

        Parameters
        ----------
        inputs : Tensor
            Embedded input sequence.

        training : bool, optional
            Enables dropout during training.

        Returns
        -------
        Tensor
            Context-aware encoder representation.
        """

        attention_output = self.attention(
            query=inputs,
            key=inputs,
            value=inputs
        )

        attention_output = self.dropout1(attention_output, training=training)

        out1 = self.layernorm1(inputs + attention_output)

        ffn_output = self.ffn(out1)

        ffn_output = self.dropout2(ffn_output, training=training)

        encoder_output = self.layernorm2(out1 + ffn_output)

        return encoder_output


# ============================================================
# Step 5: Transformer Decoder Block
# ============================================================

Header(5, "Transformer Decoder Block")

print("""
Decoder generates Marathi output.
It uses:
1. Masked Self-Attention
2. Encoder-Decoder Attention
3. Feed Forward Network
""")

class TransformerDecoder(layers.Layer):
    """
    Transformer Decoder block.

    The decoder generates the target sequence one token at a time.

    It consists of three major components:

    1. Masked Multi-Head Self-Attention
    2. Encoder-Decoder Cross Attention
    3. Feed Forward Network

    The causal mask ensures that future tokens are hidden during
    training, preventing information leakage.

    Parameters
    ----------
    embed_dim : int
        Embedding dimension.

    num_heads : int
        Number of attention heads.

    ff_dim : int
        Hidden layer size of feed-forward network.
    """


    def __init__(self, embed_dim, num_heads, ff_dim):
        """
        Initialize the Transformer Decoder.

        Parameters
        ----------
        embed_dim : int
            Size of embedding vectors.

        num_heads : int
            Number of attention heads.

        ff_dim : int
            Feed-forward network dimension.

        Returns
        -------
        None
        """
        super().__init__()

        self.masked_attention = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.encoder_decoder_attention = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=embed_dim
        )

        self.ffn = tf.keras.Sequential([
            layers.Dense(ff_dim, activation="relu"),
            layers.Dense(embed_dim)
        ])

        self.layernorm1 = layers.LayerNormalization()
        self.layernorm2 = layers.LayerNormalization()
        self.layernorm3 = layers.LayerNormalization()

        self.dropout1 = layers.Dropout(0.1)
        self.dropout2 = layers.Dropout(0.1)
        self.dropout3 = layers.Dropout(0.1)

    def get_causal_attention_mask(self, inputs):
        """
        Create a causal attention mask.

        The mask prevents the decoder from attending to future tokens
        during training.

        Example
        -------
            1 0 0 0
            1 1 0 0
            1 1 1 0
            1 1 1 1

        Parameters
        ----------
        inputs : Tensor
            Decoder input tensor.

        Returns
        -------
        Tensor
            Lower triangular attention mask.
        """
        batch_size = tf.shape(inputs)[0]
        seq_len = tf.shape(inputs)[1]

        i = tf.range(seq_len)[:, None]
        j = tf.range(seq_len)

        mask = tf.cast(i >= j, dtype="int32")
        mask = tf.reshape(mask, (1, seq_len, seq_len))

        mult = tf.concat(
            [tf.expand_dims(batch_size, -1), tf.constant([1, 1], dtype=tf.int32)],
            axis=0
        )

        return tf.tile(mask, mult)

    def call(self, decoder_inputs, encoder_outputs, training=False):
        """
        Execute the forward pass of the decoder.

        Workflow
        --------
        1. Apply masked self-attention.
        2. Perform encoder-decoder attention.
        3. Pass output through feed-forward network.
        4. Apply residual connections and layer normalization.

        Parameters
        ----------
        decoder_inputs : Tensor
            Embedded decoder input sequence.

        encoder_outputs : Tensor
            Output generated by the encoder.

        training : bool, optional
            Enables dropout during training.

        Returns
        -------
        Tensor
            Decoder output representation.
        """
        causal_mask = self.get_causal_attention_mask(decoder_inputs)

        # 1. Masked Self-Attention
        attention_output1 = self.masked_attention(
            query=decoder_inputs,
            key=decoder_inputs,
            value=decoder_inputs,
            attention_mask=causal_mask
        )

        attention_output1 = self.dropout1(attention_output1, training=training)

        out1 = self.layernorm1(decoder_inputs + attention_output1)

        # 2. Encoder-Decoder Attention
        attention_output2 = self.encoder_decoder_attention(
            query=out1,
            key=encoder_outputs,
            value=encoder_outputs
        )

        attention_output2 = self.dropout2(attention_output2, training=training)

        out2 = self.layernorm2(out1 + attention_output2)

        # 3. Feed Forward Network
        ffn_output = self.ffn(out2)

        ffn_output = self.dropout3(ffn_output, training=training)

        decoder_output = self.layernorm3(out2 + ffn_output)

        return decoder_output


# ============================================================
# Step 6: Model Building
# ============================================================

Header(6, "Complete Transformer Model Building")

print("Connecting Encoder and Decoder together.")

embed_dim = 32
num_heads = 2
ff_dim = 64

encoder_inputs = layers.Input(shape=(sequence_length,), dtype=tf.int64, name="encoder_inputs")
decoder_inputs = layers.Input(shape=(sequence_length,), dtype=tf.int64, name="decoder_inputs")

encoder_embedding = TokenAndPositionEmbedding(
    sequence_length,
    vocab_size,
    embed_dim
)(encoder_inputs)

encoder_outputs = TransformerEncoder(
    embed_dim,
    num_heads,
    ff_dim
)(encoder_embedding)

decoder_embedding = TokenAndPositionEmbedding(
    sequence_length,
    vocab_size,
    embed_dim
)(decoder_inputs)

decoder_outputs = TransformerDecoder(
    embed_dim,
    num_heads,
    ff_dim
)(decoder_embedding, encoder_outputs)

decoder_outputs = layers.Dense(vocab_size, activation="softmax")(decoder_outputs)

model = tf.keras.Model(
    [encoder_inputs, decoder_inputs],
    decoder_outputs
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()


# ============================================================
# Step 7: Training
# ============================================================

Header(7, "Model Training")

print("""
Encoder input  : English sentence
Decoder input  : Marathi sentence starting with start token
Decoder target : Marathi sentence shifted by one word
""")

decoder_target_data = np.expand_dims(decoder_target_data, -1)

model.fit(
    [encoder_input_data, decoder_input_data],
    decoder_target_data,
    epochs=300,
    batch_size=2,
    verbose=1
)


# ============================================================
# Step 8: Reverse Vocabulary for Prediction
# ============================================================

Header(8, "Reverse Vocabulary Creation")

print("Creating index-to-word dictionary for Marathi output.")

marathi_vocab = marathi_vectorizer.get_vocabulary()
index_to_word = dict(enumerate(marathi_vocab))

for i in range(15):
    print(i, ":", index_to_word.get(i, ""))


# ============================================================
# Step 9: Sentence Translation Function
# ============================================================

Header(9, "Translation Function")

print("""
During prediction, decoder generates one word at a time.
First input is 'start'.
Then predicted word is added back to decoder input.
""")

def translate_sentence(input_sentence):
    
    
    print("\nInput Sentence:", input_sentence)

    encoder_input = english_vectorizer([input_sentence])

    decoded_sentence = "start"

    for i in range(sequence_length):
        """
        Translate an English sentence into Marathi using greedy decoding.

        During inference, the decoder predicts one token at a time.
        Each predicted token is appended to the decoder input until
        the 'end' token is generated or the maximum sequence length
        is reached.

        Workflow
        --------
        1. Vectorize the English sentence.
        2. Initialize decoder with the 'start' token.
        3. Predict the next word iteratively.
        4. Stop when the 'end' token is predicted.
        5. Return the translated sentence.

        Parameters
        ----------
        input_sentence : str
            Source English sentence.

        Returns
        -------
        str
            Predicted Marathi translation.
        """

        decoder_input = marathi_vectorizer([decoded_sentence])[:, :-1]

        prediction = model.predict(
            [encoder_input, decoder_input],
            verbose=0
        )

        predicted_token_index = np.argmax(prediction[0, i, :])

        predicted_word = index_to_word.get(predicted_token_index, "")

        if predicted_word == "end" or predicted_word == "":
            break

        decoded_sentence += " " + predicted_word

    final_sentence = decoded_sentence.replace("start", "").strip()

    return final_sentence


# ============================================================
# Step 10: Final Testing
# ============================================================

Header(10, "Final Translation Testing")

test_sentences = [
    "i love ai",
    "i love python",
    "this course is good",
    "teacher explains well",
    "students are learning",
    "deep learning is powerful"
]

for sentence in test_sentences:
    output = translate_sentence(sentence)

    print("-" * 60)
    print("English :", sentence)
    print("Marathi :", output)