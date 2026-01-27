# 4. Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.

# Input : Number of elements : 11
# Input Elements :    13  5   45  7   4   56  5   34  2   5   65
# Element to search : 5
# Output : 3

def CountFrequency(List, Element):
    Count = 0

    for i in range(len(List)):
        if(List[i] == Element):
            Count = Count + 1

    return Count

def main():
    Value = 0
    Numbers = list()
    FreqEle = 0
    Ret = 0

    print("Enter the number of elements :")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        Numbers.append(int(input())) 

    print("Enter the element to count the frequency : ")
    FreqEle = int(input())

    Ret = CountFrequency(Numbers, FreqEle)
    print("Frequency of element is : ", Ret)

if __name__ == "__main__":
    main()