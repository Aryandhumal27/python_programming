# Data Shield - Automated Backup System

## Overview

Data Shield is a Python-based automated backup solution that performs incremental backups of files and folders. The system detects new or modified files using MD5 hashing, copies only the necessary files to a backup directory, and creates a compressed ZIP archive of the backup.

This approach minimizes storage usage and reduces backup time by avoiding duplicate file copies.

---

## Features

* Incremental file backup
* Detects modified files using MD5 hashing
* Preserves directory structure
* Automatic ZIP archive generation
* Scheduled backups using Python Scheduler
* Cross-platform support
* Lightweight and easy to use

---

## Technologies Used

* Python 3.x
* os
* shutil
* hashlib
* zipfile
* schedule
* sys
* time

---

## Project Structure

```
Automated_Data_Shield/
│
├── DataShield.py
├── README.md
├── requirements.txt
│
├── Data/
│   ├── file1.txt
│   ├── file2.txt
│   └── ...
│
└── Backup/
    └── (Automatically Generated)
```

---

## Working Process

### Step 1: Scan Source Directory

The application scans all files and subdirectories present in the source folder.

### Step 2: Compare Files

Each file is converted into an MD5 hash value.

The hash of the source file is compared with the corresponding backup file.

### Step 3: Incremental Backup

Files are copied only if:

* The file does not exist in the backup folder.
* The file content has changed.

### Step 4: Archive Creation

After backup completion, the backup folder is compressed into a ZIP archive with a timestamp.

Example:

```
Backup_2026-06-23_15-30-45.zip
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Aryandhumal27/python_programming.git
cd Python_projects/Automation_Projects/Automated_Data_Shield
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Display Help

```bash
python DataShield.py --h
```

### Display Usage Information

```bash
python DataShield.py --u
```

### Start Automated Backup

```bash
python DataShield.py 5 Data
```

Where:

* 5 = Backup interval in minutes
* Data = Source directory

The system will automatically perform backups every 5 minutes.

---

## Example Output

```
--------------------------------------------------
Backup Process Started Successfully At :
Tue Jun 23 15:30:45 2026
--------------------------------------------------

Backup Completed Successfully
Files Copied : 12
ZIP File Created : Backup_2026-06-23_15-30-45.zip
--------------------------------------------------
```

---

## Future Enhancements

* Email notification after backup completion
* Cloud storage integration (AWS S3, Google Drive)
* GUI dashboard using Tkinter/PyQt
* Backup history and logging
* File encryption for secure backups
* Restore functionality

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* File Handling
* Directory Traversal
* Hashing Algorithms
* Incremental Backup Strategy
* ZIP Compression
* Task Scheduling
* Automation using Python

---

## Author

**Aryan Dhumal**

---

## License

This project is developed for educational and learning purposes.

