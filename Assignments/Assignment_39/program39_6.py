# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail

# 6. Train three Decision Tree models with:
# • max_depth = 1
# • max_depth = 3
# • max_depth = None
# Compare their testing accuracies and write your observations.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def MaxDepth1():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(max_depth=1)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    
    Accuracy = accuracy_score(Y_test, Y_pred)
    print("Model Accuracy is :", Accuracy * 100, "%")

def MaxDepth3():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(max_depth=3)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)
    print("Model Accuracy is :", Accuracy * 100, "%")

def MaxDepthNone():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(max_depth=None)

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)
    print("Model Accuracy is :", Accuracy * 100, "%")


def main():
    print("Model when max_depth = 1")
    MaxDepth1()

    print("Model when max_depth = 3")
    MaxDepth3()

    print("Model when max_depth = None")
    MaxDepthNone()
    
    #  Compare their testing accuracies and write your observations.
    # Ans -> Accurcay is almost same because we work on toy dataset but in
    #         big dataset max_depth value control the complexity of the model
    
if __name__ == "__main__":
    main()

