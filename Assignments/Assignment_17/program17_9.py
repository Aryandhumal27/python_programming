# 9. Write a program which accept number from user and return number of digits in that number.
#input : 5678465      output : 7

def CountDigit(No):
    Count = 0
    while(No != 0):
        Count = Count+1
        No = int(No / 10)

    return Count

def main():
    Value = 0
    Ret = 0

    print("Enter the number :")
    Value = int(input())

    Ret = CountDigit(Value)
    print("Count of Digits is : ", Ret)

if __name__ == "__main__":
    main()