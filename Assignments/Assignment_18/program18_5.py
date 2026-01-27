# 5. Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().

# Input : Number of elements : 11
# Input Elements :    13  45  7   4   56  2   5   8   5   10  34
# Output : 54 (13 + 5 + 7 +2 + 5)

from MarvellousNum import ChkPrime

def ListPrime(List):
    Sum = 0

    for i in range(len(List)):
        if(ChkPrime(List[i]) == True):
            Sum = Sum + List[i]

    return Sum

def main():
    Value = 0
    Numbers = list()
    Ret = 0

    print("Enter the number of elements :")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        Numbers.append(int(input())) 

    Ret = ListPrime(Numbers)
    print("Addition of prime elements is", Ret)

if __name__ == "__main__":
    main()