# 8. Draw a boxplot for Attendance.
# Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    plt.boxplot(Dataset["Attendance"], patch_artist=True, boxprops=dict(facecolor="blue"))
    plt.ylabel("Attendance Percentage")
    plt.title("Boxplot of Attendance")
    plt.show()

if __name__ == "__main__":
    main()