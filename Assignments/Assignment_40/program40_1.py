# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail


# 1. After training the Decision Tree model, use:
# model.feature_importances_
# • Display importance score of each feature.
# • Which feature contributes the most in predicting FinalResult?
# • Which feature contributes the least?

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

    Feature_Imp = pd.DataFrame(
        {
            "Feature" : X_train.columns,
            "Importance" : model.feature_importances_
        }
    )

    Feature_Imp = Feature_Imp.sort_values(by="Importance", ascending=False)

    print(Feature_Imp)

    # Q1.Which feature contributes the most in predicting FinalResult?
    # Ans -> StudyHours
    
    # Which feature contributes the least?
    # Ans -> 1) Attendance
        #    2) PreviousScore
        #    3) AssignmentsCompleted
        #    4) SleepHours

if __name__ == "__main__":
    main()