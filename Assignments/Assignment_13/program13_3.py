# 1. Write a program which accepts radius of circle and prints area of circle.

def ChkPerfect(No):
    Sum = 0
    NumHalf = int(No/2) + 1
    for i in range(1, NumHalf):
        if((No % i) == 0):
            Sum = Sum + i

    if(Sum == No):
        return True
    else:
        return False


def main():
    Value = 0
    Ret = False
    
    print("Enter the number : ")
    Value = int(input())

    Ret = ChkPerfect(Value)

    if(Ret == True):
        print("It is Perfect Number")
    else:
        print("It is not a perfect Number")

if __name__ == "__main__":
    main()