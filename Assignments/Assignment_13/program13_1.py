# 1. Write a program which accepts length and width of rectangle and prints area.

def AreaOfRectangle(length, width):
    Area = 0.0
    Area = length * width
    return Area

def main():
    RectLength = 0.0
    RectWidth = 0.0
    RectArea = 0.0

    print("Enter the length of rectangle(in meter) : ")
    RectLength = float(input())
    
    print("Enter the width of rectangle(in meter) : ")
    RectWidth = float(input())

    RectArea = AreaOfRectangle(RectLength, RectWidth)

    print("Area of rectangle is :", RectArea,"Sq.m")

if __name__ == "__main__":
    main()