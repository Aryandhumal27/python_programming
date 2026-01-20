# 6. Write a lambda function which accets one number and returns True if number is Odd otherwish False.

def main():
    Value = 0
    IsOdd = False

    print("Enter the first number : ")
    Value = int(input())

    IsOdd = lambda No : True if (No % 2 != 0) else False

    if(IsOdd(Value) == True):
        print("It is Odd")
    else:
        print("It is Even")

if __name__ == "__main__":
    main()