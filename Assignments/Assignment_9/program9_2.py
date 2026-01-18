# 2. Write a program which contains one function ChkGreater() that accept two numbers abd prints the greater number.

# Input : 10  20
# Output : 20 is greater


def ChkGreater(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    value1 = 0
    value2 = 0
    Ret = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    Ret = ChkGreater(value1, value2)

    print(Ret,"is greater")
    

if __name__ == "__main__":
    main()