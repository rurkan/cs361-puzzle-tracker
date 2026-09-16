# Command Line Interface Chess Puzzle Tracker for CS361

### Disclaimers:
- This program was built with the Linux operating system in mind
  - **It has not been tested on MacOS or Windows 11**
  - I programmed it in Ubuntu 24.04 LTS on Windows Subsystem for Linux
  - It is also tested on Windows 10 in Git Bash
- The experience is best on terminals that have good Unicode and ANSI code support
- The terminal should be at least 21 characters wide to prevent the chess board from wrapping when printed
- The program does not re-calculate terminal size and the program must be restarted
##
- A chess puzzle library must be input at ./local_data/puzzles_library.csv
  - The library must be formatted as the Lichess Puzzle Library is
    - If it is not correctly formatted, the program will just crash
  - To download a puzzle library, or read the formatting, see https://database.lichess.org/#puzzles
##
- Chess move inputs must be made in UCI format
- Accounts are solely for user convenience and preference, and are stored locally, unencrypted

  - Backups of the local_data folder should be kept elsewhere to prevent data loss

## Setup

### **Prerequisites**
- Git
- Python
- Pip

### **What is Installed**
- python-chess
  - https://python-chess.readthedocs.io/en/latest/
- pandas
  - https://pandas.pydata.org/docs/

Everything is installed in a Python Virtual Environment (.venv folder) within the repo, so this will
not affect any global python installations. The run.sh script also calls the Python and Pip
installations within the .venv folder, ensuring that the correct verison is always run.

### **Installation and Running**
For Linux, BASH has been tested, other shells should work. Git Bash is recommended, or Git Bash via
the VSCode terminal.

Bash:
```bash
# BASH
./run.sh
```
The run script will check if the .venv folder exists, and if it doesn't will run the installation
script. The installation script (install.sh) can be run manually to repair broken installations.
Deletion of the local_data folder may also be necessary for a full repair.

The installation script should automatically detect which version of Python is installed, and the
operating system. 

You may have to add run permissions to  the shell file, using "chmod +x ./run.sh". 

### **Known Errors and Issues**
#### **No Puzzle Library**
```bash
#BASH
usr@pc:~/.../cs361-puzzle-tracker$ ./run.sh

Attempting to load puzzles data file, please wait! This can take a while.

ERROR: You do not currently have a puzzle library, please put it at:
        ./local_data/puzzles_library.csv

 A recommended puzzle database is the Lichess database, found at https://database.lichess.org/#puzzles

Alternatives are acceptable if they follow the Lichess database formatting
```
If you receive an error about not having a puzzle database, download or create a puzzle database,
and place it in the ./local_data folder, with the name "puzzles_library.csv". The Lichess puzzle
database comes zipped as a .zst file, and must be unzipped for use. On Linux, this can be done with
the following command if zstd is installed (often by default).
```bash
# BASH
zstd -d lichess_db_puzzle.csv.zst
```