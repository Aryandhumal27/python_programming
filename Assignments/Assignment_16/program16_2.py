# 2. Write a program which contains one function named as ChkNum() which accept one parameter as number.
# if number is even then it should display "Even number" otherwise display "Odd number" on console.

# Input : 11                  Output : Odd number
# Input : 8                   Output : Even number


def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False
        
def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = ChkNum(Value)

    if(Ret == True):
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()
