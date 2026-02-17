# Q1) Count Lines in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts how many 
# lines are present in the file.

# Input:
# Demo.txt

# Expected Output:
# Total number of lines in Demo.txt.

def main():
    lineCount = 0
    print("Enter the file Name : ")
    FileName = input()

    with open(FileName, "r") as file:
        for line in file:
            lineCount = lineCount + 1

    print(f"Total number of lines in {FileName} are : {lineCount}")

if __name__ == "__main__":
    main()