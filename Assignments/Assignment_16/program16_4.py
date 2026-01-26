# 4. Write a program which display 5 times Marvellous on screen.

# output :        Marvellous
#                 Marvellous
#                 Marvellous
#                 Marvellous
#                 Marvellous

def Display(No):
    for i in range(No):
        print("Marvellous")

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()
