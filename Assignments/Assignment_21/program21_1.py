# 1. Design a Python application that creates two threads named Prime and NonPrime.

#   -> Both threads should accept a list of integers.
#   -> The Prime tread should display all prime numbers from the list.
#   -> The NonPrime thread should display all non-prime numbers from the list.

import threading

def PrimeNum(No):
    flag = True
    NoHalf = int(No/2)

    for i in range(2, NoHalf + 1):
        if(No % i == 0):
            flag = False

    return flag

def Prime(List):
    PrimeList = list(filter(PrimeNum, List))
    print("Prime list is : ",PrimeList)
    return PrimeList

def NonPrimeNum(No):
    flag = False
    NoHalf = int(No/2)

    for i in range(2, NoHalf + 1):
        if(No % i == 0):
            flag = True

    return flag

def NonPrime(List):
    NonPrimeList = list(filter(NonPrimeNum, List))
    print("Non Prime list is : ",NonPrimeList)
    return NonPrimeList

def main():
    Value = 0
    Numbers = list()

    print("Enter the number of elements : ")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element :")
        Numbers.append(int(input()))

    t1 = threading.Thread(target= Prime, args= (Numbers, ))
    t2 = threading.Thread(target= NonPrime, args= (Numbers, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()