# 7. Write a lambda function using filter() which accepts a list of strings and returns the list of strings having length greater than 5.

def StrGreaterThan5(Data):
    result = filter((lambda Str : True if(len(Str) > 5) else False), Data)
    return list(result)

def main():
    Data = list()
    Size = 0
    Ret = list()

    print("Enter the size of data : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the",(i+1),"String : ")
        Data.append((input()))

    print("Elements of list is : ")
    print(Data)

    Ret = StrGreaterThan5(Data)
    print("Strings from Data having length greater than 5 :", Ret)

if __name__ == "__main__":
    main()