# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail

# 2. Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_pred, Y_test)

    for Actual_Value, Predicted_Value in zip(Y_test, Y_pred):
        print("Actual : ", Actual_Value , "\t" , "Predicted : ", Predicted_Value)

    print(Accuracy)

    comparison = pd.DataFrame(
        {
            "Actual" : Y_test,
            "Predicted" : Y_pred
        }
    )

    print(comparison)
if __name__ == "__main__":
    main()

