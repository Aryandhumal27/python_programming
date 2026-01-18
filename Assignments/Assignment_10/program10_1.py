# 1. Write a program which accepts one number and print multiplication table of that number.

# Input : 4
# Output : 4  8   12  16  20  24  28  32  36  40

def MulTable(No):
    for i in range(1, 11):
        print(No,"X",i,"=",(No*i))

def main():
    value = 0
    
    print("Enter the number : ")
    value = int(input())

    MulTable(value)

if __name__ == "__main__":
    main()