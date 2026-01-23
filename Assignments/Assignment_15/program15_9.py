# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

def ProductOfList(Data):
    result = reduce((lambda No1, No2 : No1 * No2), Data)
    return result

def main():
    Data = list()
    Size = 0
    Ret = 0

    print("Enter the size of data : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the",(i+1),"element : ")
        Data.append(int(input()))

    print("Elements of list is : ")
    print(Data)

    Ret = ProductOfList(Data)
    print("Product of all elements from list : ", Ret)

if __name__ == "__main__":
    main()