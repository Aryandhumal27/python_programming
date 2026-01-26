# 10. Write a program which accept name from user and display length of its name.

# Input :     Marvellous          Output :    10

def Namelength(Name):
    length = 0
    for char in Name:
        length = length + 1

    return length
    
def main():
    Ret = 0

    print("Enter the Name : ")
    Name = input()

    Ret = Namelength(Name)
    print("Length of name is :",Ret)

if __name__ == "__main__":
    main()

