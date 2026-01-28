# 2. Design a Python application that creates two thread.
#   -> Thread 1 should calculate and display the maximum element from an list.
#   -> Thread 2 should calculate and display the minimum element from the same list.
#   -> The list should be accepted from the user.

import threading

def Maximum(List):
    Max = List[0]

    for i in range(len(List)):
        if(List[i] > Max):
            Max = List[i]

    print("Maximum Element from list is :", Max)
    return Max

def Minimum(List):
    Min = List[0]

    for i in range(len(List)):
        if(List[i] < Min):
            Min = List[i]

    print("Minimum Element from list is :", Min)
    return Min

def main():
    Value = 0
    Numbers = list()

    print("Enter the number of elements : ")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element :")
        Numbers.append(int(input()))

    t1 = threading.Thread(target= Maximum, args= (Numbers, ))
    t2 = threading.Thread(target= Minimum, args= (Numbers, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()