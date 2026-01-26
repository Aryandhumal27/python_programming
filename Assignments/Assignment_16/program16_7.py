# 7. write a program which contains one function that accept one number from user and returns true if number is divisible
# by 5 otherwise return false

def ChKDivisibleBy5(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = ChKDivisibleBy5(Value)

    if(Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")


if __name__ == "__main__":
    main()
