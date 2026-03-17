# 7. Create a scatter plot of:
# StudyHours vs PreviousScore

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    pass_student = Dataset[Dataset["FinalResult"] == 1]
    fail_student = Dataset[Dataset["FinalResult"] == 0]

    plt.scatter(pass_student["StudyHours"], pass_student["PreviousScore"], color="green", label="Pass Students")
    plt.scatter(fail_student["StudyHours"], fail_student["PreviousScore"], color="red", label="Fail Students")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.title("StudyHours vs PreviousScore")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()