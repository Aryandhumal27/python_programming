# 2. Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3
# Output : 12
# Input : 6 3
# Output : 18

def main():
    Value1 = 0
    Value2 = 0

    print("Enter the first number : ")
    Value1 = int(input())
    print("Enter the second number : ")
    Value2 = int(input())

    Multiplication = lambda No1, No2 : No1*No2
    print("Multiplication is : ", Multiplication(Value1, Value2))

if __name__ == "__main__":
    main()