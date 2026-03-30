# 3. Use KNN to predict whether a student passes or fails based on study hours and attendance.


# Dataset

#    --------------------------------------
#    | Study Hours | Attendance |  Result |
#    --------------------------------------
#    |      2      |    60      |   Fail  |  
#    |      5      |    80      |   Pass  |  
#    |      6      |    85      |   Pass  |     
#    |      1      |    50      |   Fail  |  
#    --------------------------------------  

# Tasks
# 1. Accept input from user:
# ◦ Study hours
# ◦ Attendance percentage
# 2. Apply KNN algorithm
# 3. Predict whether the student Passes or Fails
# Input Example
# Enter Study Hours: 4
# Enter Attendance: 70
# Expected Output
# Predicted Result: Pass

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def main():
    data = [
        [2, 60, "Fail"],
        [5, 80, "Pass"],
        [6, 85, "Pass"],
        [1, 50, "Fail"]
    ]

    data = pd.DataFrame(data=data, columns=["Study Hours", "Attendance", "Result"])

    X = data.drop(columns=['Result'])
    Y = data['Result']

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    print("Enter Study Hours : ")
    StudyHours = int(input())

    print("Enter Attendance : ")
    Attendance = int(input())

    new_data = [[StudyHours, Attendance]]
    new_data = pd.DataFrame(new_data, columns=["Study Hours", "Attendance"])

    Result = model.predict(new_data)

    print("Predicted Result : ", Result)

if __name__ == "__main__":
    main()