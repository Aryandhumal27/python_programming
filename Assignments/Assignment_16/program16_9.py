# 9. Write a program which display first 10 even numbers on screen

# def DisplayEven():
#     EvenCount = 0
#     i = 2
#     while(EvenCount != 10):
#         print(i, end="\t")
#         EvenCount = EvenCount + 10
#         i = i + 2

def DisplayEven():
    EvenCount = 0
    i = 1
    while(EvenCount != 10):
        if(i % 2 == 0):
            print(i, end="\t")
            EvenCount = EvenCount + 1

        i = i + 1


def main():
    DisplayEven()

if __name__ == "__main__":
    main()
