# Q2) Display File Contents

# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.

# Input:
# Demo.txt

# Expected Output:
# Display contents of Demo.txt on console.

import os

def main():
    print("Enter the file name : ")
    FileName = input()

    fobj = open(FileName, "r")

    Data = fobj.read()

    print("Data from file are : \n", Data)

if __name__ == "__main__":
    main()

