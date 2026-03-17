# 6. Plot a histogram of StudyHours.
# Explain what the distribution tells you.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    plt.hist(Dataset["StudyHours"], bins=6)
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.title("Distriution of study Hours")
    plt.show()

if __name__ == "__main__":
    main()