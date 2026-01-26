# 6. Write a program which accept number from user and check
# whether that number is positive or negative or zero.

def Check(No):
    if(No == 0):
        print("Zero")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Positive Number")

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Check(Value)

if __name__ == "__main__":
    main()
