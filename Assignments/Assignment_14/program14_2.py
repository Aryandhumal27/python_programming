# 2. Write a lambda function which accepts one number and returns cube of that number.

def main():
    Value = 0
    Cube = 0

    print("Enter the number : ")
    Value = int(input())

    Cube = lambda Value : (Value**3)

    print("Cube of", Value,"is : ", Cube(Value))

if __name__ == "__main__":
    main()