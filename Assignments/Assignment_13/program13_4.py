# 4. Write a program which accepts one number and prints binary equivalent.

def IntToBinary(No):
    i = 0
    Binary = 0
    while(No != 0):
        Remainder = int(No % 2)
        Binary = Binary + (Remainder * (10 ** i))
        i = i + 1
        No = No / 2

    return Binary

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = IntToBinary(Value)
    print("Binary equivalent of", Value,"is :", Ret)

if __name__ == "__main__":
    main()