# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def BasicMathOperations(No1, No2):
    Addition = No1 + No2
    Subtraction = No1 - No2
    Multiplication = No1 * No2
    Division = No1 / No2

    print("Addition is : ", Addition)
    print("Subtraction is : ", Subtraction)
    print("Multiplication is : ", Multiplication)
    print("Division is : ", Division)

def main():
    Value1 = 0
    Value2 = 0

    print("Enter the number : ")
    Value1 = int(input())

    print("Enter the number : ")
    Value2 = int(input())

    BasicMathOperations(Value1, Value2)

if __name__ == "__main__":
    main()