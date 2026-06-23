# Automated Disk Sanitiser

## Overview

Automated Disk Sanitiser is a Python-based utility that identifies and removes duplicate files from a directory. The application uses MD5 hashing to compare file contents and accurately detect duplicate files, helping users recover disk space and maintain organized storage.

The system scans all files within a specified directory, groups files with identical content, and automatically removes redundant copies while retaining a single original file.

---

## Features

* Detect duplicate files using MD5 hashing
* Recursive directory scanning
* Automatic duplicate file removal
* Efficient checksum-based comparison
* Recover storage space
* Lightweight and easy to use
* Cross-platform support

---

## Technologies Used

* Python 3.x
* hashlib
* os

---

## Project Structure

```text
Automated_Disk_Sanitiser/
│
├── Automated_Disk_Sanitiser.py
├── README.md
├── requirements.txt
│
└── Data/
    ├── File1.txt
    ├── File2.txt
    └── ...
```

---

## Working Process

### Step 1: Directory Validation

The application verifies:

* Directory exists
* Path is a valid directory

---

### Step 2: File Scanning

The program recursively scans all files and subdirectories using:

```python
os.walk()
```

---

### Step 3: Checksum Generation

Each file is processed and converted into an MD5 hash value.

Example:

```text
5d41402abc4b2a76b9719d911017c592
```

Files with identical content generate the same checksum.

---

### Step 4: Duplicate Detection

Files are grouped according to their checksum values.

Example:

```text
Hash A
 ├── file1.txt
 ├── file2.txt
 └── file3.txt
```

Since all files share the same checksum, they are considered duplicates.

---

### Step 5: Duplicate Removal

The application:

* Keeps the first occurrence
* Deletes all remaining duplicate copies

Example:

```text
Original File     → Retained
Duplicate File 1  → Deleted
Duplicate File 2  → Deleted
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Aryandhumal27/python_programming.git
cd Python_projects/Automation_Projects/Automated_Disk_Sanitiser
```

---

## Requirements

This project uses only Python standard library modules.

No external packages are required.

```bash
python --version
```

Recommended:

```text
Python 3.8+
```

---

## Usage

### Place Files Inside Data Folder

```text
Data/
├── file1.txt
├── file2.txt
├── duplicate_file1.txt
└── duplicate_file2.txt
```

---

### Run the Program

```bash
python Automated_Disk_Sanitiser.py
```

---

## Example Output

```text
Deleted File : Data\duplicate_file1.txt
Deleted File : Data\duplicate_file2.txt

Total Deleted Files : 2
```

---

## Advantages

* Saves disk storage space
* Eliminates redundant files
* Fast checksum-based comparison
* Easy to integrate with automation workflows
* Minimal system resource usage

---

## Future Enhancements

* Graphical User Interface (GUI)
* Log file generation
* Email notification support
* Restore deleted files option
* SHA-256 based file comparison
* Scheduled automatic cleanup

---

## Learning Outcomes

This project demonstrates:

* File Handling
* Directory Traversal
* Hashing Algorithms
* Exception Handling
* Data Structures (Dictionary)
* Automation using Python
* Storage Optimization Techniques

---

## Author

**Aryan Dhumal**

---

## License

This project is developed for educational and learning purposes.

