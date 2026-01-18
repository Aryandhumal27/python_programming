# 2. Write a program which accepts one number and prints count of digits in that number.

# Input : 7521
# Output : 4

def CountDigit(No):
    DigitCount = 0
    while(No != 0):
        DigitCount = DigitCount + 1
        No = int(No / 10)

    return DigitCount

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = CountDigit(Value)

    print("Count of Digits is : ", Ret)

if __name__ == "__main__":
    main()