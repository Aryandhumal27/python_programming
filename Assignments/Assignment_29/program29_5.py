# Q5) Frequency of a String in 

# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

import sys

def main():
    frobj = open(sys.argv[1], "r")
    UserString = sys.argv[2]

    Data = frobj.read()

    words = Data.split()

    StringCount = words.count(UserString)

    print(UserString,"appers",StringCount,"times")
    
    frobj.close()

if __name__ == "__main__":
    main()

