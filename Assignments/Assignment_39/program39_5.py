# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail

# 5. Calculate:
# • Training accuracy
# • Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

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

    train_prediction = model.predict(X_train)
    train_accuracy = accuracy_score(Y_train, train_prediction)
    print("Training Accuracy : ", train_accuracy*100)

    test_prediction = model.predict(X_test)
    test_accuracy = accuracy_score(Y_test, test_prediction)
    print("Testing Accuracy : ", test_accuracy*100)

    # Q Compare both and comment whether the model is overfitting or underfitting.
    # Ans -> Both Having 100 percent accuracy model is not overfitting and underfitting

    
if __name__ == "__main__":
    main()

