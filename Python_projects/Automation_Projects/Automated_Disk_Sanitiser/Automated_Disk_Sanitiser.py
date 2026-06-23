"""
===============================================================================
Project Name : Automated Disk Sanitiser
Author       : Aryan Dhumal
Description  : Detects and removes duplicate files from a directory using
               MD5 checksum comparison.
===============================================================================
"""

import hashlib
import os


def CalculateCheckSum(FileName):
    """
    Calculate MD5 checksum of a file.

    Parameters:
        FileName (str): Path of the file.

    Returns:
        str: MD5 hash value of the file.
    """

    try:
        hobj = hashlib.md5()

        # Open file safely using context manager
        with open(FileName, "rb") as fobj:

            while True:
                Buffer = fobj.read(1024)

                if not Buffer:
                    break

                hobj.update(Buffer)

        return hobj.hexdigest()

    except Exception as e:
        print(f"Error while processing file {FileName}: {e}")
        return None


def FindDuplicate(DirectoryName="Data"):
    """
    Find duplicate files in a directory based on MD5 checksum.

    Parameters:
        DirectoryName (str): Directory to scan.

    Returns:
        dict: Dictionary containing checksum as key and list of
              file paths as values.
    """

    if not os.path.exists(DirectoryName):
        print("There is no such directory")
        return {}

    if not os.path.isdir(DirectoryName):
        print("It is not a directory")
        return {}

    Duplicate = {}

    # Traverse all files and folders recursively
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fName in FileName:

            fName = os.path.join(FolderName, fName)

            try:
                Checksum = CalculateCheckSum(fName)

                if Checksum is not None:

                    if Checksum in Duplicate:
                        Duplicate[Checksum].append(fName)
                    else:
                        Duplicate[Checksum] = [fName]

            except Exception as e:
                print(f"Error while scanning {fName}: {e}")

    return Duplicate


def DisplayResult(MyDict):
    """
    Display duplicate files found in the directory.

    Parameters:
        MyDict (dict): Dictionary returned by FindDuplicate().
    """

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0

    for value in Result:

        print("\nDuplicate File Group:")

        for subvalue in value:
            Count += 1
            print(subvalue)

        print("Total Duplicate Files :", Count)

        Count = 0


def DeleteDuplicate(Path="Data"):
    """
    Delete duplicate files from the specified directory.

    Keeps the first occurrence and removes all remaining duplicates.

    Parameters:
        Path (str): Directory to scan and clean.
    """

    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:

        for subvalue in value:

            Count += 1

            # Keep first file and delete remaining duplicates
            if Count > 1:

                try:
                    print("Deleted File :", subvalue)

                    os.remove(subvalue)

                    Cnt += 1

                except Exception as e:
                    print(f"Unable to delete {subvalue}: {e}")

        Count = 0

    print("Total Deleted Files :", Cnt)


def main():
    """
    Entry point of the application.

    Executes duplicate file detection and deletion process.
    """

    try:
        DeleteDuplicate()

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as e:
        print(f"Unexpected Error: {e}")


# Program execution starts here
if __name__ == "__main__":
    main()
