# 2. Write a program to:
# • Display total number of students in the dataset
# • Count how many students Passed (FinalResult = 1)
# • Count how many students Failed (FinalResult = 0)

import pandas as pd

def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    print("Total Number of Students in Datasets are : ", Dataset.shape[0])

    print("Student Passed : ", (Dataset['FinalResult'] == 1).sum())
    print("Student failed : ", (Dataset['FinalResult'] == 0).sum())

if __name__ == "__main__":
    main()