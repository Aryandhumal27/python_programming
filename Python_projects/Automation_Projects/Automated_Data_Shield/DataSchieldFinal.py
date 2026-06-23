"""
===============================================================================
Project Name : Data Shield
Author       : Aryan Dhumal
Description  : Automated backup system that performs incremental backups
               and creates ZIP archives at scheduled intervals.
===============================================================================
"""

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile


def make_zip(folder):
    """
    Creates a compressed ZIP archive of the specified folder.

    Parameters:
        folder (str): Name of the folder to compress.

    Returns:
        str: Generated ZIP file name.
    """

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    # Create ZIP file in write mode with compression enabled
    zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    # Traverse all files and folders recursively
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)

            # Store relative path inside ZIP instead of absolute path
            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)

    zobj.close()

    return zip_name


def calculate_hash(path):
    """
    Calculates MD5 hash of a file.

    Parameters:
        path (str): Path of the file.

    Returns:
        str: MD5 hash value of the file.
    """

    hobj = hashlib.md5()

    # Open file in binary mode
    fobj = open(path, "rb")

    # Read file in chunks to handle large files efficiently
    while True:
        data = fobj.read(1024)

        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()


def BackupFiles(Source, Destination):
    """
    Performs incremental backup.

    Copies only:
    1. New files
    2. Modified files

    Parameters:
        Source (str): Source directory path.
        Destination (str): Backup directory path.

    Returns:
        list: List of copied file names.
    """

    copied_files = []

    print("Creating backup directory...")

    # Create backup folder if it does not exist
    os.makedirs(Destination, exist_ok=True)

    # Traverse source directory recursively
    for root, dirs, files in os.walk(Source):
        for file in files:

            src_path = os.path.join(root, file)

            # Maintain same folder structure in backup directory
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy file only if:
            # 1. Backup file does not exist
            # 2. Source file content has changed
            if ((not os.path.exists(dest_path)) or
                (calculate_hash(src_path) != calculate_hash(dest_path))):

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files


def DataShieldStart(Source="Data"):
    """
    Main backup execution function.

    Steps:
    1. Perform incremental backup.
    2. Create ZIP archive.
    3. Display backup statistics.

    Parameters:
        Source (str): Source directory to backup.
    """

    Border = "-" * 50

    # Default backup directory
    BackupName = "Backup"

    print(Border)
    print("Backup Process Started Successfully At :", time.ctime())
    print(Border)

    # Copy new and modified files
    files = BackupFiles(Source, BackupName)

    # Generate ZIP archive
    zip_file = make_zip(BackupName)

    print(Border)
    print("Backup Completed Successfully")
    print("Files Copied :", len(files))
    print("ZIP File Created :", zip_file)
    print(Border)


def main():
    """
    Entry point of the application.

    Supported Operations:
    1. Help Information
    2. Usage Information
    3. Automated Backup Scheduling
    """

    Border = "-" * 50

    print(Border)
    print("---------  Data Shield System ----------")
    print(Border)

    # Handle help and usage options
    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":

            print("This script is used to:")
            print("1. Take automatic backup at scheduled intervals")
            print("2. Backup only new and modified files")
            print("3. Create ZIP archive of backup data")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":

            print("Usage:")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval    : Backup interval in minutes")
            print("SourceDirectory : Directory to be backed up")

        else:

            print("Invalid option")
            print("Use --h or --u for more information")

    # Example:
    # python DataShield.py 5 Data
    elif len(sys.argv) == 3:

        print("Inside project logic")
        print("Time Interval :", sys.argv[1])
        print("Directory Name :", sys.argv[2])

        # Schedule backup job
        schedule.every(
            int(sys.argv[1])
        ).minutes.do(
            DataShieldStart,
            sys.argv[2]
        )

        print(Border)
        print("Data Shield System Started Successfully")
        print("Backup Interval (minutes) :", sys.argv[1])
        print("Press Ctrl + C to stop execution")
        print(Border)

        # Keep scheduler running continuously
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:

        print("Invalid number of command line arguments")
        print("Use --h or --u for more information")

    print(Border)
    print("--------- Thank You For Using Our Script ---------")
    print(Border)


# Program execution starts here
if __name__ == "__main__":
    main()