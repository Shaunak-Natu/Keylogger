# keyboard Event Logger for Windows

## What is a Key Logger?

A keylogger is a type of software or hardware device that records every keystroke made on a computer keyboard. It is
designed to run in the background of a computer system without being detected by the user, and it can capture all the data
that is entered on the keyboard, including usernames, passwords, credit card numbers, and other sensitive information.

## Why is it used?

Keyloggers can be used for both legitimate and illegitimate purposes. For example, some companies use keyloggers to 
monitor employee activity on company-owned computers, while hackers may use keyloggers to steal sensitive information for
financial gain or other malicious purposes.

## Requirements

1. python3: -
You should have python3 installed in your system. You can download it from the official website.   (https://www.python.org/downloads/)

2. keyboard module: -
The keylogger detects keystrokes with the help of keyboard module. Use the command below to install
the keyboard module: -

```
pip install keyboard
```

## Usage

To use the program, simply run the keylogger.py file in Python. 

```
python keylogger.py
```

In order to actually implement it, the first step will be to create an executable file. Below are the steps to convert your python file into
a executable file with the help of pyinstaller. PyInstaller bundles a Python application and all its dependencies into a single package. The 
user can run the packaged app without installing a Python interpreter or any modules.

Step 1: First install pyinstaller package with the help of command given below: -  

```pip install pyinstaller```

Step 2: Create a .exe file with the help of pyinstaller: -

```pyinstaller -F --noconsole keylogger.py```

This command will create a standalone executable file from a Python script named name.py. For more information, visit https://pyinstaller.org/en/stable/usage.html#options

## Limitations

1. The log file is created only after the program execution is terminated.
2. The log file is stored on the targets' local machine. So, in order to retrieve the log file, you should have phsyical 
    access to the target machine.

## Output

Upon starting the program, a "log.txt" file will be created. This text file will contain a log of
all the keyboard events, including the time at which they were recorded and the key that was pressed or released. 
Here is an example of what "log.txt" looks like: -

<div align="center">
  <img src="https://user-images.githubusercontent.com/78775456/227770622-ca2419f4-b1f9-4345-af76-f688ced4ed92.png" alt="My Image">
</div>

## Acknowledgements

1. Keyboard module:
https://github.com/boppreh/keyboard

2. Time module:
https://www.geeksforgeeks.org/python-time-module/










