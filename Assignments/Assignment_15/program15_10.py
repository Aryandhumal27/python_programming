# 10. Write a lambda function using reduce() which accepts a list of numbers and returns the count of even numbers.

from functools import reduce

def CountEven(Data):
    redResult = reduce((lambda count, No : count + (1 if(No % 2 == 0) else 0)), Data, 0)
    return redResult

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

    Ret = CountEven(Data)
    print("Count of even elements is : ", Ret)
    
if __name__ == "__main__":
    main()