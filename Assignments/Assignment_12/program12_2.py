# 2. Write a program which accepts one number and prints its factors.

# Input : 12
# Output : 1  2   3   4   6   12

def Factors(No):
    factors = list()

    for i in range(1, No+1):
        if((No % i) == 0):
            factors.append(i)

    return factors

def main():
    Value = 0
    factors = list()

    print("Enter the number : ")
    Value = int(input())

    factors = Factors(Value)
    print("Factors of",Value,"is : ",factors)
    
if __name__ == "__main__":
    main()