import os
import subprocess

#Check if Python 3.9 Already Exists and Symlink Set
not_setup = False

files_to_check = [
    "/opt/conda/bin/python3",
    "/opt/conda/bin/python3.7",
    "/opt/conda/bin/python",
]

target = "/usr/bin/python3.9"

for file_path in files_to_check:
    if os.path.islink(file_path):
        link_target = os.readlink(file_path)
        if link_target == target:
            not_setup = False
        else:
            not_setup = True
    else:
        not_setup = True

if not_setup:
    #Install Python 3.9 Using Apt
    #!sudo apt update -y (optional)
    !sudo apt install python3.9 -y

    #Find the Location of Python 3.9


    result = subprocess.run(['which', 'python3.9'], stdout=subprocess.PIPE)
    print(result.stdout.decode())

    #Check if Python 3.9 is Working (ensure the location is the same as what was found in the previous cell)
    print("########TEST START########")
    !/usr/bin/python3.9 --version
    !echo 'print("Hello, World!")' > test.py
    !/usr/bin/python3.9 test.py
    print("########TEST END#########")
    print("\n")

    #Delete Python3 files and replace them with a SymLink to Python 3.9
    !sudo rm /opt/conda/bin/python3
    !sudo ln -sf /usr/bin/python3.9 /opt/conda/bin/python3
    !sudo rm /opt/conda/bin/python3.7
    !sudo ln -sf /usr/bin/python3.9 /opt/conda/bin/python3.7
    !sudo rm /opt/conda/bin/python
    !sudo ln -s /usr/bin/python3.9 /opt/conda/bin/python

#Check Python Version
print("Cells following this should be run using:")
!python --version

