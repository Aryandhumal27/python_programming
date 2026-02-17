# Q2) Count Words in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts the total 
# number of words in that file.

# Input:
# Demo.txt

# Expected Output:
# Total number of words in Demo.txt.

def main():
    WordCount = 0
    print("Enter the file Name : ")
    FileName = input()

    with open(FileName, "r") as file:
        for line in file:
            for words in line.split():
                WordCount = WordCount + 1


    print(f"Total number of words in {FileName} are : {WordCount}")

if __name__ == "__main__":
    main()