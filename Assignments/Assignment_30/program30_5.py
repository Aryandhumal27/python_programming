# Q5) Search a Word in File

# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether 
# that word is present in the file or not.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

def main():
    isFound = False

    print("Enter the source file name : ")
    FileName = input()

    print("Enter the word to search in file : ")
    WordToSearch = input()

    fsrcobj = open(FileName, "r")

    with fsrcobj as file:
        for line in file:
            for word in line.split():
                if(word == WordToSearch):
                    isFound = True
                    break

    if(isFound == True):
        print(f"{WordToSearch} is found in {FileName}")
    else:
        print(f"{WordToSearch} is not found in {FileName}")

if __name__ == "__main__":
    main()