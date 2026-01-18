# 3. Write a program which accepts one number and prints factorial of that number.

# Input : 5
# Output : 120

def Factorial(No):
    Fact = 1

    for i in range(1, No+1):
        Fact = Fact * i
    
    return Fact

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = Factorial(Value)

    print("factorial of",Value,"is : ", Ret)

if __name__ == "__main__":
    main()