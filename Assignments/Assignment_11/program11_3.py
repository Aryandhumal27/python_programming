# 3. Write a program which accepts one number and prints sum of digits.

# Input : 123
# Output : 6

def SumofDigits(No):
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = int(No / 10)

    return Sum
    
def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = SumofDigits(Value)

    print("Sum of Digits is : ", Ret)

if __name__ == "__main__":
    main()