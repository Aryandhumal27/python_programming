# 3. Write a program which accepts one number and checks whather it is palindrome or not.

# Input : 121
# Output : Palindrome

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

def IsPalindrome(No):
    ReverseNumber = ReverseDigit(No)

    if(ReverseNumber == No):
        return True
    else:
        return False
    
def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = IsPalindrome(Value)

    if(Ret == True):
        print("It is palindrome number")
    else:
        print("It is not a palindrome")
    

if __name__ == "__main__":
    main()