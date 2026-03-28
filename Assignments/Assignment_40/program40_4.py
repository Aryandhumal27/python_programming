# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail


#4. Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns="FinalResult")
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    StudyHours = [2, 4, 6, 1, 4.5]
    Attendance = [67, 43, 56, 75, 45]
    PreviousScore = [76, 56, 89, 76, 45]
    AssignmentCompleted = [3, 5, 7, 9, 0]
    SleepHours = [7, 4, 8, 5, 7]

    new_Student_details = pd.DataFrame(
        {
            "StudyHours" : StudyHours,
            "Attendance" : Attendance,
            "PreviousScore" : PreviousScore,
            "AssignmentsCompleted" : AssignmentCompleted,
            "SleepHours" : SleepHours
        }
    )

    Y_pred = model.predict(new_Student_details)

    print(Y_pred)

    new_Student_details["Prediction"] = Y_pred

    print(new_Student_details)

if __name__ == "__main__":
    main()