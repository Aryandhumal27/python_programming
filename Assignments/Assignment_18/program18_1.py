# 1. Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.

# Input : Number of elements : 6
# Input Elements :    13  5   45  7   4   56
# Output : 130

def AdditionOfList(List):
    Sum = 0

    for i in range(len(List)):
        Sum = Sum + List[i]

    return Sum

def main():
    Value = 0
    Numbers = list()
    Ret = 0

    print("Enter the number of elements :")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        Numbers.append(int(input())) 

    Ret = AdditionOfList(Numbers)
    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()