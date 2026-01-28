# 4. Design a Python application that creates two threads.
#   -> Thread 1 should compute the sum of elements from a list.
#   -> Thread 2 should compute the product of elements from the same list.
#   -> Return the results to the main thread and display them.

import threading

def Addition(List):
    Sum = 0

    for i in range(len(List)):
        Sum = Sum + List[i]

    print("Sum of list is : ", Sum)
    return Sum

def Multiplication(List):
    Product = 1

    for i in range(len(List)):
        Product = Product * List[i]

    print("Product of list is : ", Product)
    return Product

def main():
    Value = 0
    Numbers = list()

    print("Enter the number of elements : ")
    Value = int(input())

    for i in range(Value):
        print(f"Enter the {i+1} element :")
        Numbers.append(int(input()))

    t1 = threading.Thread(target= Addition, args= (Numbers, ))
    t2 = threading.Thread(target= Multiplication, args= (Numbers, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    main()