# Assignment Tasks:
# 1. Load and Explore the Dataset
# ◦ Handle missing or unknown values (e.g., unknown in categorical features).
# ◦ Display basic stats and visualize class distribution.
# 2. Preprocess the Data
# ◦ Convert categorical variables using Label Encoding or One-Hot Encoding.
# ◦ Scale numeric features (e.g., using StandardScaler).
# 3. Split the Data
# ◦ Use 80% data for training and 20% for testing.
# ◦ Apply train_test_split().
# 4. Train Classification Models
# ◦ Train the following models:
# ▪ Logistic Regression
# ▪ K-Nearest Neighbors
# ▪ Random Forest Classifier

# 5. Evaluate the Models
# ◦ Compare using:
# ▪ Accuracy
# ▪ Confusion Matrix
# ▪ Classification Report
# ▪ ROC-AUC score

# 6. Visualize Results
# ◦ Plot confusion matrix and ROC curves.

import pandas as pd
from io import StringIO

def clean_csv_format(input_file, output_file):

    cleaned_lines = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            # Remove unwanted quotes and fix formatting
            cleaned = line.strip().replace('""', '').strip('"')
            cleaned_lines.append(cleaned)

    # Write back as clean CSV
    with open(output_file, "w", encoding="utf-8") as f:
        for line in cleaned_lines:
            f.write(line + "\n")

def main():
    clean_csv_format('bank-full.csv', 'bank-formatted.csv')
    
if __name__ == "__main__":
    main()