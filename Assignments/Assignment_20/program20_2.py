# 2 Design a Python application that creates two threads named EvenFactor and OddFactor.

# Both threads should Accept one integer number as a parameter The EvenFactor thread should
# Identify all even factors of the given number Calculate and display the sum of even factors
# The OddFactor thread should : Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# after both threads complete execution, the main thread should display the message
# "Exit from main"

import threading

def EvenFactor(No):
    Sum = 0
    NoHalf = int(No/2)
    for i in range(1, NoHalf+1):
        if(No % i == 0 and i % 2 == 0):
            Sum = Sum + i

    print("Addition of Even Factors : ", Sum)

def OddFactor(No):
    Sum = 0
    NoHalf = int(No/2)
    for i in range(1, NoHalf+1):
        if(No % i == 0 and i % 2 != 0):
            Sum = Sum + i

    print("Addition of Odd Factors : ", Sum)

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    t1 = threading.Thread(target=EvenFactor, args=(Value,))
    t2 = threading.Thread(target=OddFactor, args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End from main")

if __name__ == "__main__":
    main()