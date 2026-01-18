# 4. Write a program which accept one number and prints all even numbers till that number.

# Input : 10
# Output : 2  4   6   8   10

def DisplayEven(No):
    for i in range(2,No+1, 2):
        print(i)

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    DisplayEven(Value)

if __name__ == "__main__":
    main()