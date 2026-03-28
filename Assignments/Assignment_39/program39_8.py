# Features Description
# • StudyHours – Number of hours a student studies per day.
# • Attendance – Percentage of class attendance.
# • PreviousScore – Marks obtained in the previous examination.
# • AssignmentsCompleted – Number of assignments completed by the student.
# • SleepHours – Average number of hours the student sleeps per day.
# • FinalResult – Target variable (Output):
# ◦ 1 → Pass
# ◦ 0 → Fail

# 8. Write a single structured Python program that performs:

# 1. Dataset loading
# 2. Data analysis
# 3. Visualization
# 4. Train-test split
# 5. Model training
# 6. Prediction
# 7. Accuracy calculation
# 8. Confusion matrix generation
# 9. Final conclusion
# Your code should include proper comments explaining each step.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def main():
    Border = "=" * 70

    #----------------------------------------------------------------------------------------
    # Step 1 : Dataset Loading
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 1 : Dataset Loading")
    print(Border)
    df = pd.read_csv("student_performance_ml.csv")
    print("\nDataset Load Successfully\n")

    #----------------------------------------------------------------------------------------
    # Step 2 : Data Analysis
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 2 : Data Analysis")
    print(Border)

    # Checking missing values
    print("Cheking missing values : \n")
    print(df.isnull().sum())

    # Checking Duplicates values
    print("Checking Duplicates values : \n")
    print("Duplicate values are : ",df.duplicated().sum())

    # Checking data type of columns
    print("Checking data types of columns : \n")
    print(df.dtypes)

    #----------------------------------------------------------------------------------------
    # Step 3 : Visualization
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 3 : Visualization")
    print(Border)

    print(Border)
    print("Relation between StudyHours and FinalResult")
    print(Border)

    plt.scatter(df["StudyHours"], df["FinalResult"], color="blue", label="StudyHours")
    plt.xlabel("StudyHours")
    plt.ylabel("FinalResult")
    plt.title("Relation of StudyHours and labels")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(Border)
    print("Relation between Attendance and FinalResult")
    print(Border)

    plt.scatter(df["Attendance"], df["FinalResult"], color="red", label="Attendance")
    plt.xlabel("Attendance")
    plt.ylabel("FinalResult")
    plt.title("Relation of Attendance and labels")
    plt.legend()
    plt.grid(True)
    plt.show()


    print(Border)
    print("Relation between PreviousScore and FinalResult")
    print(Border)

    plt.scatter(df["PreviousScore"], df["FinalResult"], color="green", label = "PreviousScore")
    plt.xlabel("PreviousScore")
    plt.ylabel("FinalResult")
    plt.title("Relation of PreviousScore and labels")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(Border)
    print("Relation between AssignmentsCompleted and FinalResult")
    print(Border)

    plt.scatter(df["AssignmentsCompleted"], df["FinalResult"], color="yellow", label = "AssignmentsCompleted")
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult")
    plt.title("Relation of AssignmentsCompleted and labels")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(Border)
    print("Relation between SleepHours and FinalResult")
    print(Border)

    plt.scatter(df["SleepHours"], df["FinalResult"], color="black", label="SleepHours")
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult")
    plt.title("Relation of SleepHours and labels")
    plt.legend()
    plt.grid(True)
    plt.show()

    #----------------------------------------------------------------------------------------
    # Step 4 : Train-test split
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 4 : Train-test split")
    print(Border)

    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)


    #----------------------------------------------------------------------------------------
    # Step 5 : Model training
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 5 : Model training")
    print(Border)

    model = DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    print("Model trained successfully")

    #----------------------------------------------------------------------------------------
    # Step 6 : Prediction
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 6 : Prediction")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Actual Values with Predicted Values")

    comparison = pd.DataFrame(
        {
            "Actual" : Y_test,
            "Predicted" : Y_pred
        }
    )

    print(comparison)


    #----------------------------------------------------------------------------------------
    # Step 7 : Accuracy calculation
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 7 : Accuracy calculation")
    print(Border)

    Accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Accuracy of the Model : {Accuracy*100}%")

    #----------------------------------------------------------------------------------------
    # Step 8 : Confusion matrix generation
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 8 : Confusion matrix generation")
    print(Border)

    cm = confusion_matrix(Y_test, Y_pred)

    print("Confusion Matrix : ")
    print(cm)

    #----------------------------------------------------------------------------------------
    # Step 9 : Final conclusion
    #----------------------------------------------------------------------------------------

    print(Border)
    print("Step 9 : Final conclusion")
    print(Border) 

    print(f"Model trained successfully and predict output with {Accuracy*100}% accuracy")

if __name__ == "__main__":
    main()

