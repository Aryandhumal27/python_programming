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

import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, ConfusionMatrixDisplay

def main():

    # 1. Load and Explore the Dataset
    # ◦ Handle missing or unknown values (e.g., unknown in categorical features).
    # ◦ Display basic stats and visualize class distribution.

    #------------------------------------------------------------------------------------
    # Step 1 : Load and explore the dataset
    #------------------------------------------------------------------------------------

    border = "-"*70
    
    print(border)
    print("Step 1 : Load and explore the dataset")
    print(border)

    df = pd.read_csv('bank-formatted.csv')

    print(border)
    print("Check Unknown in columns")
    print(border)
    print((df == "unknown").sum())
    print(f"Shape if dataset",df.shape)
    print(f"First 5 records of dataset : \n",df.head())
    print(f"Inforamtion of dataset columns : \n",df.info())

    print(border)
    print("Check columns that datatype is str : ")
    print(border)
    print(df.select_dtypes(include='str').columns)

    # 2. Preprocess the Data
    # ◦ Convert categorical variables using Label Encoding or One-Hot Encoding.
    # ◦ Scale numeric features (e.g., using StandardScaler)

    print(border)
    print("Step 2 : Preprocess the Data")
    print(border)

    print(border)
    print("Perform One-Hot Encoding on dataframe : ")
    print(border)
    df = pd.get_dummies(df, drop_first=True)
    print(df.shape)
    print(df.head())
    print(df.info())

    num_col = df.select_dtypes(include=["int64"]).columns
    print(num_col)

    scalar = StandardScaler()

    # 3. Split the Data
    # ◦ Use 80% data for training and 20% for testing.
    # ◦ Apply train_test_split().

    print(border)
    print("Step 3 : Split the Data")
    print(border)

    X = df.drop(columns=["y_yes"])
    Y = df["y_yes"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)

    # 4. Train Classification Models
    # ◦ Train the following models:
    # ▪ Logistic Regression
    # ▪ K-Nearest Neighbors
    # ▪ Random Forest Classifier

    print(border)
    print("Step 4 : Train Classification Models")
    print(border)

    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    model1 = KNeighborsClassifier()
    model2 = LogisticRegression()
    model3 = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model1.fit(X_train, Y_train)
    model2.fit(X_train, Y_train)
    model3.fit(X_train, Y_train)

    Y_pred1 = model1.predict(X_test)
    Y_pred2 = model2.predict(X_test)
    Y_pred3 = model3.predict(X_test)

    # 5. Evaluate the Models
    # ◦ Compare using:
    # ▪ Accuracy
    # ▪ Confusion Matrix
    # ▪ Classification Report
    # ▪ ROC-AUC score

    print(border)
    print("Step 5 : Evaluate the Models")
    print(border)
        
    Accuracy1 = accuracy_score(Y_test, Y_pred1)
    Accuracy2 = accuracy_score(Y_test, Y_pred2)
    Accuracy3 = accuracy_score(Y_test, Y_pred3)
    print("Accuracy of model1(KNN) : ", Accuracy1*100)
    print("Accuracy of model2(LR) : ", Accuracy2*100)
    print("Accuracy of model3(RT) : ", Accuracy3*100)

    cm1 = confusion_matrix(Y_test, Y_pred1)
    cm2 = confusion_matrix(Y_test, Y_pred2)
    cm3 = confusion_matrix(Y_test, Y_pred3)
    print("Confusion matrix of model1(KNN) : \n", cm1)
    print("Confusion matrix of model2(LR) : \n", cm2)
    print("Confusion matrix of model3(RT) : \n", cm3)

    cr1 = classification_report(Y_test, Y_pred1)
    cr2 = classification_report(Y_test, Y_pred2)
    cr3 = classification_report(Y_test, Y_pred3)
    print("classification report of model1(KNN) : \n", cr1)
    print("classification report of model2(LR) : \n", cr2)
    print("classification report of model3(RT) : \n", cr3)

    roc1 = roc_auc_score(Y_test, Y_pred1)
    roc2 = roc_auc_score(Y_test, Y_pred2)
    roc3 = roc_auc_score(Y_test, Y_pred3)
    print("roc_auc_score of model1(KNN) : \n", roc1)
    print("roc_auc_score of model2(LR) : \n", roc2)
    print("roc_auc_score of model3(RT) : \n", roc3)

    # 6. Visualize Results
    # ◦ Plot confusion matrix and ROC curves.   

    print(border)
    print("Step 6 : Visualize Results")
    print(border)

    disp1 = ConfusionMatrixDisplay(confusion_matrix=cm1)
    disp2 = ConfusionMatrixDisplay(confusion_matrix=cm2)
    disp3 = ConfusionMatrixDisplay(confusion_matrix=cm3)

    disp1.plot()
    plt.show()
    disp2.plot()
    plt.show()
    disp3.plot()
    plt.show()
    
if __name__ == "__main__":
    main()