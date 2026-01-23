# 8. Write a lambda function using filter() which accepts a list of numbers and returns the list of numbers divisible by both 3 and 5.

def DivibleBy3And5(Data):
    result = filter((lambda No : True if(((No % 3) == 0) and ((No % 5) == 0)) else False), Data)
    return list(result)

def main():
    Data = list()
    Size = 0
    Ret = list()

    print("Enter the size of data : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the",(i+1),"element : ")
        Data.append(int(input()))

    print("Elements of list is : ")
    print(Data)

    Ret = DivibleBy3And5(Data)
    print("Elements from Data that are divisible by 3 and 5 : ", Ret)

if __name__ == "__main__":
    main()