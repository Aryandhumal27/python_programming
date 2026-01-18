# write a program which accept one number and print square of that number

def Square(No):
    Ans = 0
    Ans = No * No
    return Ans

def main():
    Ret = 0
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = Square(Value)

    print("Square of", Value ,"is : ", Ret)

if __name__ == "__main__":
    main()