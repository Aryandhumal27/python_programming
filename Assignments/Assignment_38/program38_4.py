# 4. Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

import pandas as pd

def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    print("Percentage of Pass Students : ")
    
    percentages = Dataset['FinalResult'].value_counts(normalize=True)

    print("Percentage of Pass students are : ", percentages[1] * 100,"%")
    print("Percentage of Fail students are : ", percentages[0] * 100,"%")

    # Is the dataset balanced? Justify your answer.
    # Ans -> Yes, Dataset is Balance because its contains 60% of Pass student records 
    #         and 40% percent of Fail students record that means dateset contains suffient
    #         amount of records to train the model for predictions.

if __name__ == "__main__":
    main()