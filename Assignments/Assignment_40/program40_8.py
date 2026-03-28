# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail


# 8. Decision Tree Visualization
# Use:
# from sklearn.tree import plot_tree
# Visualize the trained decision tree.
# • Which feature appears at the root node?
# • Why do you think that feature was selected first?

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
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

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy is : ", Accuracy * 100)

    plt.figure(figsize=(15, 10))

    plot_tree(
        model,                     # your trained model
        feature_names=X.columns,   # column names
        class_names=[str(c) for c in model.classes_], 
        filled=True               # adds colors
    )

    plt.show()    

if __name__ == "__main__":
    main()