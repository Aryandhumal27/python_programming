# 1 Design a Python application that creates two separate threads named Even and Odd.

# -> The Even thread should display the first 10 even numbers.
# -> The Odd thread should display the first 10 odd numbers
# -> Both threads should execute independently using the threading module.
# -> Ensure proper thread creation and execution

import threading

def FirstTenEven():
    EvenCount = 0
    i = 1

    while(EvenCount < 10):
        if(i % 2 == 0):
            EvenCount = EvenCount + 1
            print(i, end="\t")

        i = i + 1

    print()

def FirstTenOdd():
    OddCount = 0
    i = 1

    while(OddCount < 10):
        if(i % 2 != 0):
            OddCount = OddCount + 1
            print(i, end="\t")

        i = i + 1

    print()

def main():
    t1 = threading.Thread(target = FirstTenEven)
    t2 = threading.Thread(target = FirstTenOdd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
