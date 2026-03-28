# 9. Create a new column:

# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature.
# Does accuracy improve?

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv('student_performance_ml.csv')

    df["PerformanceIndex"] = df["StudyHours"] * 2 + df["Attendance"]

    # print(df["PerformancrIndex"])
    # print(df)

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print(model.feature_importances_)
    # Feature importance of preformanceIndex is 0
    # There is no impact on accuracy

    print("Accuracy is : ", Accuracy*100)


if __name__ == "__main__":
    main()