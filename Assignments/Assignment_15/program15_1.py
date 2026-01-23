# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

def main():
    Data = list()
    Squares = list()
    Size = 0

    print("Enter the size of data : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the",(i+1),"element : ")
        Data.append(int(input()))

    print("Elements of list is : ")
    print(Data)

    Squares = map((lambda No : No**2), Data)
    print("Squares of list is :", list(Squares))
    
if __name__ == "__main__":
    main()