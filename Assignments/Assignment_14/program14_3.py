# 3. Write a lambda function which accepts two number and returns maximum number.

def main():
    Value1 = 0
    Value2 = 0
    Maximum = 0

    print("Enter the first number : ")
    Value1 = int(input())

    print("Enter the second number : ")
    Value2 = int(input())

    Maximum = lambda No1, No2 : No1 if(No1 > No2) else No2

    print("Maximum is : ", Maximum(Value1, Value2))

if __name__ == "__main__":
    main()