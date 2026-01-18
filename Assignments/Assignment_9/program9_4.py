# 4. Write a program which accept one number and prints cube of that number.

def Cube(No):
    Ans = 0
    Ans = No * No * No
    return Ans

def main():
    Ret = 0
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = Cube(Value)

    print("Cube of", Value ,"is : ", Ret)

if __name__ == "__main__":
    main()