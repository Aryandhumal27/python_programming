# 2. Using the same dataset from above question, calculate model performance.

# Tasks
# 1. Predict all Y values using regression equation.
# 2. Calculate:
# • Mean Squared Error (MSE)
# • R2 Score
# Show all intermediate calculations.

def main():
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    X_Mean = sum(X) / len(X)
    Y_Mean = sum(Y) / len(Y)

    Numerator = 0
    Denominator = 0
    R2_Denominator = 0
    MSE_Numerator = 0

    for i in range(len(X)):
        Numerator = Numerator + (X[i] - X_Mean) * (Y[i] - Y_Mean)
        Denominator = Denominator + (X[i] - X_Mean)**2
        R2_Denominator = T=R2_Denominator + (Y[i] - Y_Mean)**2

    slope = Numerator / Denominator
    intercept = Y_Mean - (slope * X_Mean)

    print(f"Mean of X = {X_Mean}")
    print(f"Mean of Y = {Y_Mean}")
    print(f"Slope(m) = {slope}")
    print(f"Intercept (c) = {intercept}")

    print("\nRegression Equation:")
    print(f"Y = {slope}X + {intercept}")

    print("\nPredicted Values:")
    for i in range(len(X)):
        predicted = slope * X[i] + intercept
        MSE_Numerator = MSE_Numerator + (Y[i] - predicted)**2
        print(f"Predicted Y for X = {X[i]} : {predicted}")

    MSE = MSE_Numerator / len(X)
    R2 = 1 - (MSE_Numerator / R2_Denominator)

    print("\nMean Squared Error (MSE):", MSE)
    print("R2 Score:", R2)


if __name__ == "__main__":
    main()