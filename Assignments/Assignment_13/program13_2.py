# 1. Write a program which accepts radius of circle and prints area of circle.

from math import pi

def AreaOfCircle(radius):
    Area = 0.0
    Area = pi * (radius**2)
    return Area
    

def main():
    CircleRadius = 0.0
    CircleArea = 0.0

    print("Enter the radius of circle : ")
    CircleRadius = float(input())

    CircleArea = AreaOfCircle(CircleRadius)

    print("Area of circle is :", CircleArea)

if __name__ == "__main__":
    main()