# 10. Write a lambda function which accepts three numbers and return laregst number.

from functools import reduce

def main():
    Values = list()
    Maximum = 0

    for i in range(1, 4):
        print("Enter the", i, "number : ")
        Values.append(int(input()))

    Maximum = reduce((lambda No1, No2 : No1 if(No1 > No2) else No2), Values)

    print("Maximum is : ", Maximum)

if __name__ == "__main__":
    main()