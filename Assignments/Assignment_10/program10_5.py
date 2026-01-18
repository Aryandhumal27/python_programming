# 5. Write a program which accept one number and prints all Odd numbers till that number.


def DisplayOdd(No):
    for i in range(1,No+1, 2):
        print(i)

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    DisplayOdd(Value)

if __name__ == "__main__":
    main()