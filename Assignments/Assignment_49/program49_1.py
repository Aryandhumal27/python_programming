# Objective:
# Build a Machine Learning model to predict whether a patient is diabetic (1) or not (0) based on medical
# attributes.

# Task Instructions:
# You must complete the following steps
# 1. Exploratory Data Analysis (EDA):
# • Load the dataset using pandas.
# • Display the first 5 rows.
# • Show column info and check for null values.
# • Display basic statistics using .describe().
# • Plot the distribution of the target variable (Outcome).
# • Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.

# 2. Data Preprocessing:
# • Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
# • Apply feature scaling using StandardScaler or MinMaxScaler.
# • Split the dataset into features (X) and target (y).

# 3. Model Building:
# Train at least 2 different algorithms on the dataset:
# • Logistic Regression
# • K-Nearest Neighbors (KNN)
# • Decision Tree
# • Use train_test_split to divide the data.

# 4. Model Evaluation:
# • Print accuracy score, confusion matrix, precision, recall, and F1 score.
# • Use matplotlib or seaborn to visualize confusion matrix.


# 5. Final Output:
# • Predict whether a patient is diabetic based on test data.
# • Display predictions on screen and save them in a CSV file.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score, ConfusionMatrixDisplay

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

def main():
    # 1. Exploratory Data Analysis (EDA):
    # • Load the dataset using pandas.
    # • Display the first 5 rows.
    # • Show column info and check for null values.
    # • Display basic statistics using .describe().
    # • Plot the distribution of the target variable (Outcome).
    # • Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.

    border = "-"*70

    print(border)
    print("Step 1 : Exploratory Data Analysis (EDA):")
    print(border)

    # Load the dataset using pandas.
    df = pd.read_csv('diabetes.csv')

    # Display the first 5 rows.
    print(border)
    print("Display first 5 rows")
    print(border)
    print(df.head())

    # Show column info and check for null values
    print(border)
    print("Show column info and check for null values")
    print(border)
    print(df.info())

    # Display basic statistics using .describe()
    print(border)
    print("Display basic statistics using .describe().")
    print(border)
    print(df.describe())

    # 2. Data Preprocessing:
    # • Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
    # • Apply feature scaling using StandardScaler or MinMaxScaler.
    # • Split the dataset into features (X) and target (y).

    print(border)
    print("Step 2 : Data Preprocessing")
    print(border)

    # Check if any columns that contains 0
    print(border)
    print("Check if any columns that contains 0")
    print(border)
    print((df == 0).sum())

    # replace 0 with NaN to detect by inbuid function
    df[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] = df[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]].replace(0, np.nan)

    # Now Check for null values
    print(border)
    print("Columns contain nan values")
    print(border)
    print(df.isna().sum())

    # Replace NaN value with median
    Col_Cont_NaN = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in Col_Cont_NaN:
        df[col] = df[col].fillna(df[col].median())

    # Now Check for null values after removing null values
    print(border)
    print("Columns contain nan values after removing null values")
    print(border)
    print(df.isna().sum())

    X = df.drop(columns="Outcome")
    Y = df["Outcome"]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    scalar = StandardScaler()

    X_data = X_test

    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    # 3. Model Building:
    # Train at least 2 different algorithms on the dataset:
    # • Logistic Regression
    # • K-Nearest Neighbors (KNN)
    # • Decision Tree
    # • Use train_test_split to divide the data.

    print(border)
    print("Step 3 : Model Building")
    print(border)

    # Create Objects of model
    model_lr = LogisticRegression(max_iter=5000)
    model_dt = DecisionTreeClassifier(random_state=42)
    model_knn = KNeighborsClassifier(n_neighbors=5)

    # Train all the model
    model_lr.fit(X_train, Y_train)
    model_dt.fit(X_train, Y_train)
    model_knn.fit(X_train, Y_train)

    # Create model of votingClassifier 
    hard_model = VotingClassifier(
        estimators=[
            ("lr", model_lr),
            ("dt", model_dt),
            ("knn", model_knn),
        ],
        voting='hard'
    )

    # Train the model
    print(border)
    print("Train the model")
    print(border)
    hard_model.fit(X_train, Y_train)

    print("Model Trained Successfully")

    # Test the model
    print(border)
    print("Test the model")
    print(border)
    Y_pred = hard_model.predict(X_test)

    print("Model Test Successfully")

    # 4. Model Evaluation:
    # • Print accuracy score, confusion matrix, precision, recall, and F1 score.
    # • Use matplotlib or seaborn to visualize confusion matrix.

    print(border)
    print("Step 4 : Model Evaluation")
    print(border)
    # Evaluation of the model
    # Check the Accuracy of the model
    Accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy is : ", Accuracy)

    cm = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix : \n", cm)

    # Display COnfusion matrix
    display_cm = ConfusionMatrixDisplay(confusion_matrix=cm)
    display_cm.plot()
    plt.show()

    precision = precision_score(Y_test, Y_pred)
    print("Precision Scaore are : ", precision)

    recall = recall_score(Y_test, Y_pred)
    print("Recall Score are : ", recall)

    f1Score = f1_score(Y_test, Y_pred)
    print("F1 Score are : ", f1Score)    

    cr = classification_report(Y_test, Y_pred)
    print("Classification Report : \n", cr)   

    # 5. Final Output:
    # • Predict whether a patient is diabetic based on test data.
    # • Display predictions on screen and save them in a CSV file.

    print(border)
    print("Step 5 : Final Output")
    print(border)

    Data = pd.DataFrame(data=X_data)
    Data["Prediction"] = Y_pred

    Data.to_csv("diabetes_Predicted_Data.csv")

    print("diabetes_Predicted_Data.csv created successfully")

if __name__ == "__main__":
    main()