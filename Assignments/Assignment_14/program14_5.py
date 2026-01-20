# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False. 

def main():
    Value = 0
    IsEven = False

    print("Enter the first number : ")
    Value = int(input())

    IsEven = lambda No : True if (No % 2 == 0) else False

    if(IsEven(Value) == True):
        print("It is Even")
    else:
        print("It is Odd")


if __name__ == "__main__":
    main()