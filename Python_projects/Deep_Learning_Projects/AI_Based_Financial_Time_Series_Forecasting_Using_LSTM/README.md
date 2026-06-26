# 📈 AI-Based Financial Time Series Forecasting Using LSTM

An end-to-end Deep Learning project that predicts future stock prices using **Long Short-Term Memory (LSTM)** networks. The project demonstrates complete financial time series forecasting, including data preprocessing, sequence generation, LSTM architecture, model training, evaluation, visualization, and next-day stock price prediction.

---

## 🚀 Project Overview

Financial markets generate sequential data where previous trends influence future values. Traditional machine learning algorithms struggle to capture long-term dependencies, whereas **LSTM (Long Short-Term Memory)** networks are specifically designed for sequential data.

This project forecasts the **next day's Reliance stock closing price** using historical closing prices.

---

## 🎯 Objectives

- Load and preprocess stock market data
- Perform Min-Max normalization
- Create time-series sequences
- Build and train an LSTM neural network
- Predict future stock prices
- Evaluate model performance using regression metrics
- Visualize actual vs predicted prices
- Forecast the next day's closing price

---

## 📂 Project Structure

```
AI_Based_Financial_Time_Series_Forecasting_Using_LSTM/
│
├── reliance_LSTM_time_series.py
├── reliance_stock_sample.csv
├── requirements.txt
├── README.md
│
├── actual_vs_predicted_detailed.png
├── training_loss_detailed.png
├── reliance_prediction_output.csv
└── reliance_lstm_detailed_model.h5
```

---

## 🛠 Technologies Used

- Python 3.10+
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

## 🧠 Deep Learning Algorithm

### Long Short-Term Memory (LSTM)

LSTM is a specialized Recurrent Neural Network (RNN) capable of learning long-term dependencies in sequential data.

It consists of:

- Forget Gate
- Input Gate
- Candidate Memory
- Output Gate

These gates allow the network to selectively remember or forget information over long sequences, making it highly effective for financial forecasting.

---

## ⚙️ Workflow

1. Load historical stock data
2. Convert Date column into datetime format
3. Extract Close Price
4. Apply Min-Max Scaling
5. Generate time-series sequences
6. Reshape data for LSTM
7. Build stacked LSTM model
8. Train model with Early Stopping
9. Predict stock prices
10. Convert predictions back to original scale
11. Evaluate using MAE, MSE, RMSE
12. Plot graphs
13. Predict next day's closing price

---

## 📊 Model Architecture

```
Input Layer
      │
      ▼
LSTM (50 Units)
      │
Dropout (0.2)
      │
LSTM (50 Units)
      │
Dropout (0.2)
      │
Dense (25, ReLU)
      │
Dense (1)
      │
Predicted Stock Price
```

---

## 📈 Evaluation Metrics

The project evaluates forecasting performance using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 📉 Output

The project generates:

- Predicted stock prices
- Actual vs Predicted graph
- Training loss graph
- CSV containing predictions
- Trained LSTM model (.h5)

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/Aryandhumal27/python_programming.git
```

### Move to Project Folder

```bash
cd Python_projects/Deep_Learning_Projects/AI_Based_Financial_Time_Series_Forecasting_Using_LSTM
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python AI_Based_Financial_Time_Series_Forecasting.py
```

---

## 📌 Dataset

Sample Dataset:

- Historical Reliance Stock Prices
- CSV Format
- Features include:
  - Date
  - Open
  - High
  - Low
  - Close
  - Volume

---

## 📚 Learning Outcomes

After completing this project, you will understand:

- Financial Time Series Forecasting
- Sequence Generation
- Min-Max Scaling
- LSTM Networks
- Deep Learning Regression
- Time Series Prediction
- Model Evaluation
- Data Visualization

---

## 🔮 Future Improvements

- Multi-stock forecasting
- GRU implementation
- Bidirectional LSTM
- Hyperparameter tuning
- Attention Mechanism
- Technical Indicators (RSI, EMA, MACD)
- Real-time stock prediction
- Live data using financial APIs

---

## 👨‍💻 Author

**Aryan Dhumal**

Computer Engineering Student

GitHub:
https://github.com/Aryandhumal27

---

## ⭐ If you found this project useful, don't forget to star the repository.
