# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers, List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

def main():
    Value = 0
    data = list()

    print("enter the number of elements : ")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        data.append(int(input()))

    filterList = list(filter((lambda No : True if(No >= 70 and No <= 90) else False), data))
    print("List after filter =", filterList)

    mapList = list(map(lambda No : No + 10, filterList))
    print("List after map =", mapList)

    reduceResult = reduce(lambda No1, No2 : No1*No2, mapList)
    print("Output of reduce =", reduceResult)

if __name__ == "__main__":
    main()