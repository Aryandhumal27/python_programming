# 🌐 Transformer Neural Machine Translation (Encoder–Decoder)

A complete implementation of a **Transformer-based Neural Machine Translation (NMT)** model using **TensorFlow/Keras**. This project demonstrates how the **Encoder–Decoder Transformer architecture** translates English sentences into Marathi using **Multi-Head Attention**, **Positional Embeddings**, and **Greedy Decoding**. The implementation follows the core principles introduced in the original Transformer architecture, where an encoder processes the source sentence and a decoder generates the target sentence autoregressively. 

---

## 📌 Project Overview

Neural Machine Translation (NMT) is a Natural Language Processing (NLP) task that automatically translates text from one language to another while preserving its meaning.

This project implements a simplified Transformer model from scratch using TensorFlow. Instead of relying on pre-trained models, every major Transformer component is implemented manually for educational purposes.

The project covers:

- English → Marathi Translation
- Tokenization and Text Vectorization
- Positional Embeddings
- Multi-Head Self-Attention
- Encoder–Decoder Attention
- Feed Forward Networks
- Greedy Decoding
- End-to-End Model Training

---

# 🚀 Features

- ✅ Custom Transformer Encoder
- ✅ Custom Transformer Decoder
- ✅ Token + Positional Embedding Layer
- ✅ Multi-Head Self-Attention
- ✅ Encoder–Decoder Cross Attention
- ✅ Causal Attention Mask
- ✅ Teacher Forcing during Training
- ✅ Greedy Decoding during Prediction
- ✅ TensorFlow / Keras Functional API
- ✅ Well-Commented Industrial Code

---

# 🏗️ Project Architecture

```
                 English Sentence
                        │
                        ▼
                Text Vectorization
                        │
                        ▼
          Token + Positional Embedding
                        │
                        ▼
                Transformer Encoder
                        │
                        ▼
                 Encoder Output
                        │
                        ▼
              Transformer Decoder
       (Masked Attention + Cross Attention)
                        │
                        ▼
              Dense + Softmax Layer
                        │
                        ▼
               Marathi Translation
```

---

# 📂 Project Structure

```
Transformer_Neural_Machine_Translation_Encoder_Decoder/
│
├── Transformer_Neural_Machine_Translation_Encoder_Decoder.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Technologies Used

- Python 3.x
- TensorFlow
- Keras
- NumPy

---

# 📚 Transformer Workflow

## Step 1 – Dataset Creation

A small English–Marathi parallel corpus is created for demonstration.

Example:

```
English:
I love AI

Marathi:
Start mala ai avadte End
```

---

## Step 2 – Text Vectorization

The TextVectorization layer converts sentences into integer token sequences.

Example:

```
I love python

      ↓

[15, 6, 20, 0, 0, 0, 0, 0]
```

---

## Step 3 – Token & Positional Embedding

Each token is converted into a dense embedding vector.

Since Transformers process all words simultaneously, positional embeddings are added so the model understands word order.

---

## Step 4 – Transformer Encoder

The encoder processes the complete English sentence.

Components:

- Multi-Head Self-Attention
- Feed Forward Network
- Layer Normalization
- Residual Connections
- Dropout

---

## Step 5 – Transformer Decoder

The decoder predicts one word at a time.

It contains:

- Masked Self-Attention
- Encoder–Decoder Attention
- Feed Forward Network

A causal attention mask prevents the decoder from accessing future words during training.

---

## Step 6 – Model Building

The complete encoder-decoder architecture is connected using the Keras Functional API.

```
   Encoder
      │
      ▼
Encoder Output
      │
      ▼
    Decoder
      │
      ▼
    Dense
      │
      ▼
    Softmax
```

---

## Step 7 – Model Training

Training uses:

- Adam Optimizer
- Sparse Categorical Crossentropy
- Teacher Forcing

---

## Step 8 – Reverse Vocabulary

Creates an index-to-word dictionary for converting predicted token IDs back into Marathi words.

---

## Step 9 – Translation

During inference:

1. Encode English sentence
2. Start decoder with **start** token
3. Predict one word
4. Append prediction
5. Repeat until **end** token

This process is called **Greedy Decoding**.

---

## Step 10 – Testing

Example:

```
Input:
I love AI

   ↓

Output:
mala ai avadte
```

---

# 🧠 Classes Implemented

## TokenAndPositionEmbedding

Responsible for:

- Token Embedding
- Positional Embedding

---

## TransformerEncoder

Implements:

- Multi-Head Self Attention
- Feed Forward Network
- Residual Connections
- Layer Normalization

---

## TransformerDecoder

Implements:

- Masked Self Attention
- Encoder–Decoder Attention
- Feed Forward Network
- Causal Attention Mask

---

# 📈 Model Hyperparameters

| Parameter | Value |
|------------|--------|
| Vocabulary Size | 1000 |
| Sequence Length | 8 |
| Embedding Dimension | 32 |
| Attention Heads | 2 |
| Feed Forward Units | 64 |
| Epochs | 300 |
| Batch Size | 2 |

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Aryandhumal27/python_programming.git
```

Move to the project folder:

```bash
cd Python_projects/Deep_Learning_Projects/Transformer_Neural_Machine_Translation_Encoder_Decoder
```

Install dependencies:

```bash
pip install tensorflow numpy
```

Run the project:

```bash
python Transformer_Neural_Machine_Translation_Encoder_Decoder.py
```

---

# 📌 Learning Outcomes

After completing this project, you will understand:

- Transformer Architecture
- Encoder–Decoder Models
- Self Attention
- Multi-Head Attention
- Positional Encoding
- Cross Attention
- Teacher Forcing
- Greedy Decoding
- Neural Machine Translation
- TensorFlow Custom Layers

---

# 🔮 Future Improvements

- Larger multilingual datasets
- Byte Pair Encoding (BPE)
- Beam Search Decoding
- BLEU Score Evaluation
- Attention Visualization
- Transformer Base Architecture
- Model Checkpointing
- GPU Training
- TensorBoard Integration

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is intended for educational and learning purposes.

---

# 👨‍💻 Author

**Aryan Dhumal**

Computer Science Engineer

Interested in:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Natural Language Processing
- Data Science

GitHub:
https://github.com/Aryandhumal27
