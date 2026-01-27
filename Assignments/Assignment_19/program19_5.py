# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def ChkPrime(No):
    flag = True
    Nohalf = int(No/2)

    for i in range(2, Nohalf+1):
        if(No % i == 0):
            flag = False
            break

    return flag

def main():
    Value = 0
    data = list()

    print("enter the number of elements : ")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        data.append(int(input()))

    filterList = list(filter(ChkPrime, data))
    print("List after filter =", filterList)

    mapList = list(map(lambda No : No*2, filterList))
    print("List after map =", mapList)

    reduceResult = reduce(lambda No1, No2 : No1 if(No1>No2) else No2, mapList)
    print("Output of reduce =", reduceResult)

if __name__ == "__main__":
    main()