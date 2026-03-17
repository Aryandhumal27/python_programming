# 3. Using pandas functions, calculate and display:
# • Average StudyHours
# • Average Attendance
# • Maximum PreviousScore
# • Minimum SleepHours

import pandas as pd

def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    print("Average of StudyHours : ", Dataset['StudyHours'].mean())
    print("Average of Attendance : ", Dataset['Attendance'].mean())
    print("Maximum PreviousScore : ", Dataset['PreviousScore'].max())
    print("Minimum SleepHours : ", Dataset['SleepHours'].min())

if __name__ == "__main__":
    main()