# 3. Design a Python application that created two threads named EvenList and OddList.

# -> Both threads should accept a list of integers as input.
# -> The EvenList thread should:
#       -> Extraxt all even elements from the list.
#       -> Calculate and display their sum.
# -> The OddList thread should:
#       -> Extraxt all odd elements from the list.
#       -> Calculate and display their sum.
# -> Threads should run concurrently.


import threading
from functools import reduce

def EvenList(List):
    Result = list()

    for i in range(len(List)):
        if(List[i] % 2 == 0):
            Result.append(List[i])

    Sum = reduce((lambda A,B : A + B), Result)
    print("Addition of Even elements is : ", Sum)

def OddList(List):
    Result = list()

    for i in range(len(List)):
        if(List[i] % 2 != 0):
            Result.append(List[i])

    Sum = reduce((lambda A,B : A + B), Result)
    print("Addition of Odd elements is : ", Sum)

def main():
    Value = 0
    Numbers = list()

    print("Enter the number of elements : ")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element : ")
        Numbers.append(int(input()))

    t1 = threading.Thread(target=EvenList, args=(Numbers,))
    t2 = threading.Thread(target=OddList, args=(Numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End from main")

if __name__ == "__main__":
    main()