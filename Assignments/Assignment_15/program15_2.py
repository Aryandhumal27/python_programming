# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers./

def FilterEven(Data):
    Evenlist = list()
    Evenlist = filter((lambda No : True if(No % 2 == 0) else False), Data)
    return list(Evenlist)


def main():
    Data = list()
    EvenNumber = list()
    Size = 0

    print("Enter the size of data : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the",(i+1),"element : ")
        Data.append(int(input()))

    print("Elements of list is : ")
    print(Data)

    EvenNumber = FilterEven(Data)
    print("Even numbers list is : ", EvenNumber)

if __name__ == "__main__":
    main()