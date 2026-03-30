# 1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using any machine learning library.
# The program should:

# • Calculate Euclidean distance
# • Sort distances
# • Select K nearest neighbors
# • Predict the class based on majority voting

# Dataset

#    ---------------------------------
#    | Point |  X   |   Y   | Labels |
#    ---------------------------------
#    |   A   |  1   |   2   |  Red   |
#    |   B   |  2   |   3   |  Red   |
#    |   C   |  3   |   1   |  Blue  |   
#    |   D   |  6   |   5   |  Blue  |
#    ---------------------------------   

# Tasks
# 1. Accept X and Y coordinates of a new point from the user.
# 2. Compute Euclidean distance from all dataset points.
# 3. Sort the distances.
# 4. Select K = 3 nearest neighbors.
# 5. Predict the class label.
    
# Input Format
# Enter X coordinate: 2
# Enter Y coordinate: 2

# Expected Output
# Nearest Neighbors:
# A - Distance: 1.0
# B - Distance: 1.0
# C - Distance: 1.41

# Predicted Class: Red

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
        {'Point' : 'D', 'X' : 6, 'Y' : 5, 'Labels' : 'Blue'}
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

    k = 3
    RedCount = 0
    BlueCount = 0

    print("Nearest Neighbors : ")
    for i in range(k):
        print(f"{data[i]['Point']} - Distance : {data[i]['EuclideanDistance']}")
        if data[i]['Labels'] == 'Red':
            RedCount = RedCount + 1
        elif data[i]['Labels'] == 'Blue':
            BlueCount = BlueCount + 1

    
    if(RedCount > BlueCount):
        print("Prdicted Class : Red")
    else:
        print("Predicted Class : Blue")


if __name__ == "__main__":
    main()