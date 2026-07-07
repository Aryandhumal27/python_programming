# Transformer Sentiment Classification (Encoder Only)

A deep learning project that demonstrates **Encoder-Only Transformer architecture** for **binary text sentiment classification** using **TensorFlow** and **Keras**.

This project is designed for educational purposes to explain every stage of a Transformer Encoder, including text preprocessing, embeddings, self-attention, Transformer Encoder blocks, model training, evaluation, and prediction.

---

## 📌 Features

* Encoder-Only Transformer Architecture
* Custom Token & Position Embedding Layer
* Multi-Head Self Attention
* Feed Forward Neural Network
* Layer Normalization
* Residual Connections
* Dropout Regularization
* Binary Sentiment Classification
* Step-by-step output with explanations
* Beginner-friendly implementation

---

## 📂 Project Structure

```
Text_Sentiment_Analysis_Encoder_Only/
│
├── Transformer_Sentiment_Classification_Encoder_Only.py
├── README.md
```

---

## 🛠 Technologies Used

* Python 3.x
* TensorFlow
* Keras
* NumPy

---

## 📚 Transformer Architecture

```
Input Text
      │
      ▼
Text Vectorization
      │
      ▼
Token IDs
      │
      ▼
Token Embedding
      │
      ▼
Position Embedding
      │
      ▼
Token + Position Embedding
      │
      ▼
Multi-Head Self Attention
      │
      ▼
Add & Layer Normalization
      │
      ▼
Feed Forward Network
      │
      ▼
Add & Layer Normalization
      │
      ▼
Global Average Pooling
      │
      ▼
Dense Layer (ReLU)
      │
      ▼
Dropout
      │
      ▼
Dense Layer (Sigmoid)
      │
      ▼
Sentiment Prediction
```

---

## 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/Aryandhumal27/python_programming.git
```

Navigate to the project directory.

```bash
cd Python_projects/Deep_Learning_Projects/Text_Sentiment_Analysis_Encoder_Only
```

Install the required packages.

```bash
pip install tensorflow numpy
```

---

## ▶️ Run the Project

```bash
python Transformer_Sentiment_Classification_Encoder_Only.py
```

---

## 📖 Workflow

### Step 1 – Dataset Creation

* Create positive and negative training sentences.
* Assign binary labels.

### Step 2 – Text Preprocessing

* Convert text into tokens.
* Create vocabulary.
* Apply padding.

### Step 3 – Embedding Layer

* Generate Token Embeddings.
* Generate Position Embeddings.
* Combine both embeddings.

### Step 4 – Self Attention

* Apply Multi-Head Self Attention.
* Compute attention scores.
* Generate contextual word representations.

### Step 5 – Token and Position Embedding Layer

* Custom Keras layer.
* Reusable embedding module.

### Step 6 – Transformer Encoder

The encoder block contains:

* Multi-Head Self Attention
* Residual Connection
* Layer Normalization
* Feed Forward Network
* Dropout

### Step 7 – Model Building

The model consists of:

* Input Layer
* Embedding Layer
* Transformer Encoder
* Global Average Pooling
* Dense Layer
* Dropout
* Sigmoid Output Layer

### Step 8 – Model Training

* Adam Optimizer
* Binary Crossentropy Loss
* Accuracy Metric

### Step 9 – Evaluation

Evaluate model performance using:

* Training Loss
* Training Accuracy

### Step 10 – Prediction

Predict sentiment for unseen sentences.

Example output:

```
Sentence : this session is good

Prediction : Positive

Score : 0.96
```

---

## 📊 Model Hyperparameters

| Parameter                 |               Value |
| ------------------------- | ------------------: |
| Vocabulary Size           |                1000 |
| Sequence Length           |                   8 |
| Embedding Dimension       |                  16 |
| Number of Attention Heads |                   2 |
| Feed Forward Dimension    |                  32 |
| Batch Size                |                   2 |
| Epochs                    |                  80 |
| Optimizer                 |                Adam |
| Loss Function             | Binary Crossentropy |

---

## 📈 Learning Objectives

This project demonstrates:

* Text preprocessing
* Tokenization
* Padding
* Word Embedding
* Positional Embedding
* Self Attention
* Multi-Head Attention
* Transformer Encoder
* Feed Forward Networks
* Residual Connections
* Layer Normalization
* Binary Text Classification

---

## 👨‍💻 Author

**Aryan Dhumal**

Computer Science Engineering Student

Deep Learning | Machine Learning | Artificial Intelligence | Python Developer

GitHub: https://github.com/Aryandhumal27

---

## ⭐ Future Improvements

* Larger real-world datasets
* Train on IMDB Reviews
* Pre-trained BERT encoder
* Attention visualization
* Model checkpointing
* Early stopping
* Confusion Matrix
* Precision, Recall and F1-Score
* TensorBoard integration
* Model deployment using Flask or FastAPI

---

## 📄 License

This project is developed for educational and learning purposes. Feel free to use, modify, and enhance it for academic and personal projects.

