# 3. Consider below task

    # 1. Train linear regression model.
    # 2. Predict salary for 6 years of experience.
    # 3. Plot regression line using matplotlib.

# Dataset
    #  ---------------------------
    #  | Experience   |   Salary |
    #  ---------------------------
    #  |     1        |   20000  |
    #  |     2        |   25000  |
    #  |     3        |   30000  |
    #  |     4        |   35000  |
    #  |     5        |   40000  |
    #  ---------------------------
# Expected Output
# Predicted Salary for 6 Years Experience: ₹45000
# Graph should display:
# • Data points
# • Regression line

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

def main():
    data = {
        "Experience": [1, 2, 3, 4, 5],
        "Salary": [20000, 25000, 30000, 35000, 40000]
    }

    data = pd.DataFrame(data)

    X = data[["Experience"]]
    Y = data["Salary"]

    print(data)

    model = LinearRegression()

    model.fit(X, Y)

    new_data = [[6]]
    new_data = pd.DataFrame(data=new_data, columns=["Experience"])

    PredictedSalary = model.predict(new_data)

    print(f"Predicted Salary for 6 Years Experience: {PredictedSalary}")

    plt.scatter(X, Y, label="Actual Data")
    X_line = np.linspace(1, 6, 100).reshape(-1, 1)
    Y_line = model.predict(X_line)
    plt.plot(X_line, Y_line, label= "Regression Line")
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()