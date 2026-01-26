# 6. Write a program which accept one number and display below pattern.
# input : 5
# Output :
#             *   *   *   *   *
#             *   *   *   *
#             *   *   *
#             *   *
#             *   

def Display(No):
    for i in range(No):
        print("*\t"*(No-i))

def main():
    Value = 0

    print("Enter the number :")
    Value = int(input())

    Display(Value)


if __name__ == "__main__":
    main()