# 3. Design a Python application where multiple threads update a shared variable.
#   -> Use a Lock to avoid rare conditions.
#   -> Each thread should increment the shared counter multiple times.
#   -> Display the final value of the counter after all threads complete execution.


import threading

Counter = 0
lobj = threading.Lock()

def IncrementCounter():
    global Counter

    for i in range(10):
        with lobj:
            Counter = Counter + 5
            print(Counter)

def main():
    t1 = threading.Thread(target=IncrementCounter)
    t2 = threading.Thread(target=IncrementCounter)
    t3 = threading.Thread(target=IncrementCounter)
    t4 = threading.Thread(target=IncrementCounter)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("End of main")

if __name__ == "__main__":
    main()