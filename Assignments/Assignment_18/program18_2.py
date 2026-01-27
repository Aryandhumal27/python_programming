# 2. Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.

# Input : Number of elements : 7
# Input Elements :    13  5   45   7   4   56 34
# Output : 56

def Maximum(List):
    Max = List[0]

    for i in range(len(List)):
        if(List[i] > Max):
            Max = List[i]

    return Max

def main():
    Value = 0
    Numbers = list()
    Ret = 0

    print("Enter the number of elements :")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        Numbers.append(int(input())) 

    Ret = Maximum(Numbers)
    print("Maximum element is : ", Ret)

if __name__ == "__main__":
    main()