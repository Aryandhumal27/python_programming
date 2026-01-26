# 9. Write a program which accept number from user and return addition of digits in that number.
#input : 5678465      output : 41

def AdditionOfDigits(No):
    Addition = 0
    Digit = 0
    Sum = 0
    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = int(No / 10)

    return Sum

def main():
    Value = 0
    Ret = 0

    print("Enter the number :")
    Value = int(input())

    Ret = AdditionOfDigits(Value)
    print("Addition of Digits is : ", Ret)

if __name__ == "__main__":
    main()