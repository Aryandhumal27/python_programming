# 3. Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.

# Input : Number of elements : 4
# Input Elements :    13  5   45  7
# Output : 5

def Minimum(List):
    Min = List[0]

    for i in range(len(List)):
        if(List[i] < Min):
            Min = List[i]

    return Min

def main():
    Value = 0
    Numbers = list()
    Ret = 0

    print("Enter the number of elements :")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        Numbers.append(int(input())) 

    Ret = Minimum(Numbers)
    print("Minimum element is : ", Ret)

if __name__ == "__main__":
    main()