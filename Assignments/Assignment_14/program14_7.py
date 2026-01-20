# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

def main():
    Value = 0
    IsDivisibleBy5 = False

    print("Enter the number : ")
    Value = int(input())

    IsDivisibleBy5 = lambda No : True if (No % 5 == 0) else False

    if(IsDivisibleBy5(Value) == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")


if __name__ == "__main__":
    main()


