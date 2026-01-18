# 5. Write a program which accept one number and check whether it is divisible by 3 and 5

# Input : 15
# Output : Divisible by 3 and 5

def ChkDivisible(No):
    if(((No % 3) == 0) and ((No % 5) == 0)):
        return True
    else:
        return False
    
def main():
    value = 0
    Ret = False

    print("Enter the Number : ")
    value = int(input())

    Ret = ChkDivisible(value)

    if(Ret == True):
        print(value, "is Divisible by 3 and 5")
    else:
        print(value, "is not Divisible by 3 and 5")

if __name__ == "__main__":
    main()