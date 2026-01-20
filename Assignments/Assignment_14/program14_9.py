# 9. Write a lambda function which accepts two numbers and returns multiplication.

def main():
    Value1 = 0.0
    Value2 = 0.0
    Multiplication = 0.0

    print("Enter the first number : ")
    Value1 = float(input())

    print("Enter the second number : ")
    Value2 = float(input())

    Multiplication = lambda No1, No2 : No1 * No2

    print("Multiplication is :", Multiplication(Value1, Value2))

if __name__ == "__main__":
    main()