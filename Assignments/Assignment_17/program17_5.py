# 5. Write a program which accept one number for user and check whether number is prime or not
# Input : 5       Output : It is prime number


def ChkPrime(No):
    isPrime = True
    NoHalf = int(No/2)
    for i in range(2, NoHalf+1):
        if(No % i == 0):
            isPrime = False
            
    return isPrime

def main():
    Value = 0
    Ret = False

    print("Enter the number :")
    Value = int(input())

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()