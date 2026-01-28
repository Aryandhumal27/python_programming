# 3 Write a Python program to implement a class named Arithmetic with the following characteristics:

#   -> The class should contain two instance variables: Valuel and Value2.
#   -> Define a constructor (init) that initializes all instance variables to 0.
#   -> Implement the following instance methods:
#       -> Accept() - accepts values for Valuel and Value2 from the user.
#       -> Addition() - returns the addition of Valuel and Value2.
#       -> Subtraction() - returns the subtraction of Valuel and Value2.
#       -> Multiplication() - returns the multiplication of Valuel and Value2.
#       -> Division() - returns the division of Valuel and Value2 (handle division by zero properly).
#   ->Create multiple objects of the Arithmetic class and invoke all the instance methods


class Arithmatic:
    def __init__(self):
        self.Value1 = 0.0
        self.value2 = 0.0

    def Accept(self):
        print("Enter the first number : ")
        self.Value1 = float(input())

        print("Enter the Second number : ")
        self.Value2 = float(input())

    def Addition(self):
        Add = 0.0
        Add = self.Value1 + self.Value2
        return Add
    
    def Subtraction(self):
        Sub = 0.0
        Sub = self.Value1 - self.Value2
        return Sub
    
    def Multiplication(self):
        Mul = 0.0
        Mul = self.Value1 * self.Value2
        return Mul
    
    def Division(self):
        Div = 0.0
        Div = self.Value1 / self.Value2
        return Div
    
def main():
    obj1 = Arithmatic()
    obj2 = Arithmatic()
    obj3 = Arithmatic()
    obj4 = Arithmatic()

    obj1.Accept()
    print("Addition is of obj1 is :", obj1.Addition())
    print("Subtraction is of obj1 is :", obj1.Subtraction())
    print("Multiplication is of obj1 is :", obj1.Multiplication())
    print("Division is of obj1 is :", obj1.Division())
    print()

    obj2.Accept()
    print("Addition is of obj2 is :", obj2.Addition())
    print("Subtraction is of obj2 is :", obj2.Subtraction())
    print("Multiplication is of obj2 is :", obj2.Multiplication())
    print("Division is of obj2 is :", obj2.Division())
    print()

    obj3.Accept()
    print("Addition is of obj3 is :", obj3.Addition())
    print("Subtraction is of obj3 is :", obj3.Subtraction())
    print("Multiplication is of obj3 is :", obj3.Multiplication())
    print("Division is of obj3 is :", obj3.Division())
    print()

    obj4.Accept()
    print("Addition is of obj4 is :", obj4.Addition())
    print("Subtraction is of obj4 is :", obj4.Subtraction())
    print("Multiplication is of obj4 is :", obj4.Multiplication())
    print("Division is of obj4 is :", obj4.Division())
    print()

    print("End of main")

if __name__ == "__main__":
    main()

