# keylogger Implementation in Python.


## What is a Key Logger?
   A keylogger is a type of software or hardware device that records every keystroke made on a computer keyboard. It is
designed to run in the background of a computer system without being detected by the user, and it can capture all the data
that is entered on the keyboard, including usernames, passwords, credit card numbers, and other sensitive information.

## Why is it used?
   Keyloggers can be used for both legitimate and illegitimate purposes. For example, some companies use keyloggers to 
monitor employee activity on company-owned computers, while hackers may use keyloggers to steal sensitive information for
financial gain or other malicious purposes.

## My Implementation: -

### Features: -

  1. Logs all keystrokes on the target machine.
  2. The .exe file can be run on any windows machine.

### Working: -

   Two things happen when the keylog() function is called. Firstly, a keyboard object is created and it begins recording all
the keystrokes. Secondly, a text file named "log" is created. The Keyboard object then writes all the keystrokes into a text file.

### Problems / Errors I faced and how I solved them : -

1. No idea about what python libraries I was going to use: -

    At first I was clueless about how I was going to record all the keystrokes, what modules was I going to use and how was I going to log it. After some research I read about the keyboard module. Keyboard module detects all the keyboard events with a simple .record() function. 

2. making of the .exe file: -

### Some ideas on how can my keylogger be used in the real world: -

1. email: -

2. usb: -
