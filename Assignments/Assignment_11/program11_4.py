# 3. Write a program which accepts one number and prints reverse of that number.

# Input : 123
# Output : 321

def CountDigit(No):
    DigitCount = 0
    while(No != 0):
        DigitCount = DigitCount + 1
        No = int(No / 10)

    return DigitCount

def ReverseDigit(No):
    Digit = 0
    TotalDigit = CountDigit(No)
    ReverseNum = 0

    while(No != 0):
        Digit = No % 10
        ReverseNum = ReverseNum + (Digit * (10**(TotalDigit-1)))
        TotalDigit = TotalDigit - 1
        No = int(No / 10)

    return ReverseNum
    
def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = ReverseDigit(Value)

    print("Reverse Number is : ", Ret)

if __name__ == "__main__":
    main()