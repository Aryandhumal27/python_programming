# 1. Write a program which contains one lambda function which accepts one parameter and return
# power of two.

# Input : 4
# Output : 16

# Input : 6
# Output : 64

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Square = lambda No : No**2
    print("Square of number is : ", Square(Value))

if __name__ == "__main__":
    main()