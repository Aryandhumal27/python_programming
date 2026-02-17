# Q4) Compare Two Files (Command Line)

# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.

# • If both files contain the same contents, display Success
# • Otherwise display Failure

# Input (Command Line):
# Demo.txt Hello.txt

# Expected Output:
# Success OR Failure

import sys

def main():
    frobj1 = open(sys.argv[1], "r")

    Data1 = frobj1.read()

    frobj2 = open(sys.argv[2], "r")

    Data2 = frobj2.read()

    if(Data1 == Data2):
        print("Content in both files are same")
    else:
        print("Content in both files are different")

    frobj1.close()
    frobj2.close()

if __name__ == "__main__":
    main()

