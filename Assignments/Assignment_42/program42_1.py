# 1. Implement Simple Linear Regression manually without using any ML library.

# Dataset
# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]

# Tasks
# Calculate:
# 1. Mean of X (X̄ )
# 2. Mean of Y (Ȳ)
# 3. Slope (m)
# 4. Intercept (c)

# Expected Output Example
# Mean of X = 3
# Mean of Y = 3.6
# Slope (m) = 0.4
# Intercept (c) = 2.4

# Regression Equation:
# Y = 0.4X + 2.4
# Predicted Y for X = 6 : 4.8

def main():
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    X_Sum = 0
    for i in X:
        X_Sum = X_Sum + i

    X_Mean = X_Sum / len(X)

    Y_Sum = 0
    for i in Y:
        Y_Sum = Y_Sum + i

    Y_Mean = Y_Sum / len(Y)

    Numerator = 0
    Denominator = 0
    for i in range(len(X)):
        Numerator = Numerator + ((X[i] - X_Mean) * (Y[i] - Y_Mean))
        Denominator = Denominator + ((X[i] - X_Mean)**2)

    slope = Numerator/Denominator

    Intercept = Y_Mean - (slope*X_Mean)

    print(f"Mean of X = {X_Mean}")
    print(f"Mean of Y = {Y_Mean}")
    print(f"Slope(m) = {slope}")
    print(f"Intercept (c) = {Intercept}")

    print("Regression Equation : ")
    print(f"Y = {slope}X + {Intercept}")

    PredictedValue = (slope*6) + Intercept

    print("Predicted Y for X = 6 : ", PredictedValue)   

if __name__ == "__main__":
    main()