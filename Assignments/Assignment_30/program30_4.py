# Q4) Copy File Contents into Another File

# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.

# Input:
# ABC.txt Demo.txt

# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

def main():
    print("Enter the source file name : ")
    SrcFileName = input()

    print("Enter the destination file name : ")
    DestFileName = input()

    fsrcobj = open(SrcFileName, "r")
    fdestobj = open(DestFileName, "w")

    Data = fsrcobj.read()

    fdestobj.write(Data)

    print("file copied successfully")

if __name__ == "__main__":
    main()