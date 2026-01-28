# 2. Write a Python program to implement a class named Circle with the following requirements:
#   -> The class should contain three instance variables: Radius, Area, and Circumference.
#   -> The class should contain one class variable named PI, initialized to 3.14.
#   -> Define a constructor (init) that initializes all instance variables to 0.0.
#   -> Implement the following instance methods:
#       -> Accept() - accepts the radius of the circle from the user.
#       -> CalculateArea() - calculates the area of the circle and stores it in the Area variable.
#       -> Calculate Circumference() - calculates the circumference of the circle and stores it in the Circumference variable.
#       -> Display() - displays the values of Radius, Area, and Circumference.
#   -> Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the radius of the circle :")
        Value = float(input())
        self.Radius = Value

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * (Circle.PI * self.Radius)

    def Display(self):
        print("Radius of the circle are :", self.Radius)
        print("Area of the circle are :", self.Area)
        print("Circumference of the circle are :", self.Circumference)

def main():
    obj1 = Circle()
    obj2 = Circle()
    obj3 = Circle()
    obj4 = Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

    obj3.Accept()
    obj3.CalculateArea()
    obj3.CalculateCircumference()
    obj3.Display()

    obj4.Accept()
    obj4.CalculateArea()
    obj4.CalculateCircumference()
    obj4.Display()
    
    print("End of main")

if __name__ == "__main__":
    main()
    