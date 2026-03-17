# 9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    plt.scatter(Dataset["AssignmentsCompleted"], Dataset["FinalResult"], color = "blue")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")
    plt.title("relationship between AssignmentsCompleted and FinalResult")
    plt.show()

    # Observation :

    # Students who complete more assignments are more likely to pass.
    # Students with less completed assignments tend to fail.

if __name__ == "__main__":
    main()