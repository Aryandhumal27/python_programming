# 1. Write a lambda function which accepts one number and returns square of that number.

def main():
    Value = 0
    Square = 0

    print("Enter the number : ")
    Value = int(input())

    Square = lambda Value : (Value**2)

    print("Square of", Value,"is : ", Square(Value))

if __name__ == "__main__":
    main()