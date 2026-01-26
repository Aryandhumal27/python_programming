# 4. Write a program which accept one number form user and return addition of its factors.
# Input : 12          Output : 16 (1, 2, 3, 4, 6)


def AdditionOfFact(No):
    NoHalf = int(No/2)
    Sum = 0
    for i in range(1, NoHalf+1):
        if(No % i == 0):
            Sum = Sum + i
    return Sum

def main():
    Value = 0
    Ret = 0

    print("Enter the number :")
    Value = int(input())

    Ret = AdditionOfFact(Value)

    print("Addition of factors is : ", Ret)

if __name__ == "__main__":
    main()