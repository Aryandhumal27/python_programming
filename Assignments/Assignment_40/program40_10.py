# 10. Train model with:

# • max_depth = None

# Calculate:
# • Training accuracy
# • Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv('student_performance_ml.csv')

    df["PerformanceIndex"] = df["StudyHours"] * 2 + df["Attendance"]

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(max_depth=None)

    model.fit(X_train, Y_train)

    X_pred = model.predict(X_train)
    Y_pred = model.predict(X_test)

    Training_Accuracy = accuracy_score(Y_train, X_pred)
    Testing_Accuracy = accuracy_score(Y_test, Y_pred)

    print(model.feature_importances_)

    print("Traning Accuracy is : ", Training_Accuracy*100)
    print("Testing Accuracy is : ", Testing_Accuracy*100)

if __name__ == "__main__":
    main()