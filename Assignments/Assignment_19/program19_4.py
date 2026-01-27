# 4. Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204


from functools import reduce

def main():
    Value = 0
    data = list()

    print("enter the number of elements : ")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        data.append(int(input()))

    filterList = list(filter((lambda No : True if(No % 2 == 0) else False), data))
    print("List after filter =", filterList)

    mapList = list(map(lambda No : No**2, filterList))
    print("List after map =", mapList)

    reduceResult = reduce(lambda No1, No2 : No1+No2, mapList)
    print("Output of reduce =", reduceResult)

if __name__ == "__main__":
    main()