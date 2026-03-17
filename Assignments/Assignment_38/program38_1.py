# 1. Write a Python program to load the file student_performance_ml.csv using pandas.
# Display:
# • First 5 records
# • Last 5 records
# • Total number of rows and columns
# • List of column names
# • Data types of each column

import pandas as pd

def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    
    print(Border)
    print("First 5 records of dataset are : ")
    print(Border)
    print(Dataset.head())

    print()

    print(Border)
    print("Last 5 records of dataset are : ")
    print(Border)
    print(Dataset.tail())

    print()

    print(Border)
    print("Total Number of Rows and columns are : ")
    print(Border)
    Dimension = Dataset.shape
    print("Total Number of Rows in dataset : ", Dimension[0])
    print("Total Number of Columns in dataset : ", Dimension[1])

    print()

    print(Border)
    print("Data types of each column : ")
    print(Border)
    print(Dataset.dtypes)

if __name__ == "__main__":
    main()