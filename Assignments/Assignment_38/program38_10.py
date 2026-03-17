# 10. Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Border = "-"*100
    Dataset = pd.read_csv('student_performance_ml.csv')

    plt.scatter(Dataset["SleepHours"], Dataset["FinalResult"], color = "blue")
    plt.xlabel("SleepHours")
    plt.ylabel("Final Result")
    plt.title("relationship between SleepHours and FinalResult")
    plt.show()

    # Does sleeping more guarantee success?
    # Ans -> Sleeping more does not guarantee success.
    #        many students who sleep around 6–8 hours pass,
    #     some students with similar sleep hours still fail. 
    #     Therefore, sleep alone cannot determine the final result,
    #     other factors like study hours, attendance, and assignments
    #     also affect performance.

    
if __name__ == "__main__":
    main()