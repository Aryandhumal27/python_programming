# 3. Write a program which accept one number from user and return its factorial.
# Input : 5                   Output : 120

def Factorial(No):
    Mul = 1
    for i in range(1, No+1):
        Mul = Mul * i
    return Mul
    
def main():
    Value = 0
    Ret = 0

    print("Enter the number :")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorial is : ", Ret)

if __name__ == "__main__":
    main()