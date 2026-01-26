# 8. Write a program which accept number from user and print that number of "*" on screen

def Display(No):
    for i in range(No):
        print("*\t", end="")

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()
