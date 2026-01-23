# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers./

def FilterOdd(Data):
    Oddlist = list()
    Oddlist = filter((lambda No : True if(No % 2 != 0) else False), Data)
    return list(Oddlist)


def main():
    Data = list()
    OddNumber = list()
    Size = 0

    print("Enter the size of data : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the",(i+1),"element : ")
        Data.append(int(input()))

    print("Elements of list is : ")
    print(Data)

    OddNumber = FilterOdd(Data)
    print("Odd numbers list is : ", OddNumber)

if __name__ == "__main__":
    main()