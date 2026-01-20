# 8. Write a lambda function which accepts two numbers and returns addition.

def main():
    Value1 = 0.0
    Value2 = 0.0
    Add = 0.0

    print("Enter the first number : ")
    Value1 = float(input())

    print("Enter the second number : ")
    Value2 = float(input())

    Add = lambda No1, No2 : No1 + No2

    print("Addition is :", Add(Value1, Value2))

if __name__ == "__main__":
    main()