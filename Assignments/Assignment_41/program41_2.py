# 2. The value of K plays an important role in the KNN algorithm.
# Write a Python program that demonstrates how prediction changes when K changes.
# Dataset
# Use the same dataset as Assignment 1.
# Tasks
# Predict the class of the same new point using:
# • K = 1
# • K = 3
# • K = 5
# Expected Output
# Prediction Results
# K = 1 → Red
# K = 3 → Red
# K = 5 → Blue
# Explain why the prediction changes when K increases.

from math import sqrt

def Euclidean(data, X, Y):
    EuclideanDistance = []
    for i in range(len(data)):
        dist = sqrt(((data[i]['X'] - X)**2) + ((data[i]['Y'] - Y)**2))
        EuclideanDistance.append(dist)

    return EuclideanDistance

def main():
    data = [
        {'Point' : 'A', 'X' : 1, 'Y' : 2, 'Labels' : 'Red'},
        {'Point' : 'B', 'X' : 2, 'Y' : 3, 'Labels' : 'Red'},
        {'Point' : 'C', 'X' : 3, 'Y' : 1, 'Labels' : 'Blue'},
        {'Point' : 'D', 'X' : 6, 'Y' : 5, 'Labels' : 'Blue'},
    ]

    print("Enter the coordinate of X : ")
    X = int(input())

    print("Enter the coordinate of Y : ")
    Y = int(input())

    EuclideanDistance = Euclidean(data, X, Y)

    for i in range(len(data)):
        dist = EuclideanDistance[i]
        data[i]['EuclideanDistance'] = dist

    data = sorted(data, key= lambda d : d['EuclideanDistance'])

    RedCount = 0
    BlueCount = 0

    for k in range(1,6):
        print("Nearest Neighbors : ")
        old = k
        if(k > len(data)):
            k = len(data)
        for i in range(k):
            if(i > len(data)):
                i = len(data)

            print(f"{data[i]['Point']} - Distance : {data[i]['EuclideanDistance']}")
            if data[i]['Labels'] == 'Red':
                RedCount = RedCount + 1
            elif data[i]['Labels'] == 'Blue':
                BlueCount = BlueCount + 1

        k = old

        print(f"For k = {k} :")
        if(RedCount > BlueCount):
            print("Prdicted Class : Red\n")
        else:
            print("Predicted Class : Blue\n")


if __name__ == "__main__":
    main()