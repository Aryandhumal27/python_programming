# 2. Write a program which accept one number and prints sum of first N natural numbers.

# Input : 5
# Output : 15

def SumNatural(No):
    Sum = 0

    for i in range(1, No+1):
        Sum = Sum + i
    
    return Sum

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = SumNatural(Value)

    print("Sum of first", Value, "natural numbers is : ", Ret)

if __name__ == "__main__":
    main()