# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail


# 6. Identify students where:
# y_test != y_pred
# • Display those rows.
# • How many students were misclassified?
# • What common pattern do you observe?

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Reattempt this que
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

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy is : ", Accuracy*100)

    Arr = Y_test != Y_pred

    print(Arr)




if __name__ == "__main__":
    main()