# 5. Based on the dataset values, analyze whether:
# • Higher StudyHours increase the chance of passing.
# • Higher Attendance improves FinalResult.
# Write your observations in 4–5 lines.

import pandas as pd

def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    # Q1-> Ans : Based of dataset after analyze the values of column
    #             StudyHours if value is greater than 4 is increase the
    #             chance of passing. if it is less than 4 then FinalResult
    #             is Fail according to the dataset therefore Higher StudyHours
    #             increase the chance of passing.

    #Q2-> Ans : Based of dataset after analyze the values of column
    #             Attendance. if value is greater than 75 is Improve 
    #             FinalResult. if it is less than equal to 75 then FinalResult
    #             is Fail according to the dataset therefore Higher Attendance
    #             Improve FinalResult.

if __name__ == "__main__":
    main()