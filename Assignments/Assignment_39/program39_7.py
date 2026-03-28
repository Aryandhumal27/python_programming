# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail

# 7. Use the trained model to predict result for a student with:
    
# • StudyHours = 6
# • Attendance = 85
# • PreviousScore = 66
# • AssignmentsCompleted = 7
# • SleepHours = 7
# Will the student Pass or Fail?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    Student_Record = pd.DataFrame(data=[[6, 85, 66, 7, 7]], columns=["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"])

    Student_Prediction = model.predict(Student_Record)

    for Prediction in Student_Prediction:
        if(Prediction == 1):
            print("Student Pass")
        else:
            print("Student Fail")

if __name__ == "__main__":
    main()

