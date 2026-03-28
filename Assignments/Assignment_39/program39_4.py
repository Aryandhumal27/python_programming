# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail

# 4. Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.

# Explain clearly:
# • True Positive
# • True Negative
# • False Positive
# • False Negative

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    for Actual_Value, Predicted_Value in zip(Y_test, Y_pred):
        print("Actual : ", Actual_Value , "\t" , "Predicted : ", Predicted_Value)

    comparison = pd.DataFrame(
        {
            "Actual" : Y_test,
            "Predicted" : Y_pred
        }
    )

    print(comparison)

    Accuracy = accuracy_score(Y_test, Y_pred)
    print("Model Accuracy is :", Accuracy * 100, "%")

    def ConfusionMatrixDisplay(Y_test, Y_pred):
        cm = confusion_matrix(Y_test, Y_pred)
        print(cm)

    print("Displying confusion matrix : ")
    ConfusionMatrixDisplay(Y_test, Y_pred)

    # 1) True Positive
    # -> Correctly predited Positive
    # -> Actual Value = 0
    # -> Predicted value = 0

    # 2) True Negative
    # -> Correctly predited Negative
    # -> Actual Value = 1
    # -> Predicted value = 1

    # 3) False positive
    # -> incorrectly predited Positive when actual value is negative
    # -> Actual Value = 1
    # -> Predicted value = 0

    # 4) False Negative
    # -> incorrectly predited Negative when actual value is Positive
    # -> Actual Value = 0
    # -> Predicted value = 1

    
if __name__ == "__main__":
    main()

