# 1. Write a program which accepts one number and checks whether it is prime or not.

# Input : 11
# Output : Prime Number

def IsPrime(No):
    flag = True
    Nohalf = (int)(No/2)
    for i in range(2, (Nohalf+1)):
        if((No % i) == 0):
            flag = False
            break

    return flag

def main():
    Value = 0
    Ret = False

    print("Enter the number : ")
    Value = int(input())

    Ret = IsPrime(Value)

    if(Ret == True):
        print(Value,"is prime number")
    else:
        print(Value,"is not a prime number")

if __name__ == "__main__":
    main()