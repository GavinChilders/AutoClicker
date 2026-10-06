#=======================================================================
# Auto Clicker Macro
# This script will continuously click at the current mouse position
# until you stop it by pressing a predefined key
#
# Author: Gavin Childers
# Date: 2026-04-01
# Last Updated: 2026-10-06
#
# Version 0.2.0 -- Early Stage
#=======================================================================

# Imports
import time
import threading
import tkinter as tk

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


#=======================================================================
# Auto Clicker Class
#=======================================================================

class AutoClicker(threading.Thread):

    def __init__(self, delay, button):
        super().__init__(daemon=True)

        self.delay = delay
        self.button = button

        self.click_event = threading.Event()
        self.stop_event = threading.Event()

        self.mouse = Controller()

    def start_clicking(self):
        self.click_event.set()

    def stop_clicking(self):
        self.click_event.clear()

    def exit(self):
        self.stop_clicking()
        self.stop_event.set()

    def update_config(self, delay=None, button=None):
        if delay is not None:
            self.delay = delay

        if button is not None:
            self.button = button

    def run(self):
        while not self.stop_event.is_set():

            if self.click_event.is_set():
                self.mouse.click(self.button)
                time.sleep(self.delay)

            else:
                time.sleep(0.01)


#=======================================================================
# Application
#=======================================================================

class AutoClickerApp:

    def __init__(self, root):

        self.root = root

        #---------------------------------------------------------------
        # Default Configuration
        #---------------------------------------------------------------

        self.delay = 0.001
        self.button = Button.left

        self.start_key = KeyCode(char="a")
        self.exit_key = KeyCode(char="b")

        #---------------------------------------------------------------
        # Auto Clicker
        #---------------------------------------------------------------

        self.clicker = AutoClicker(
            self.delay,
            self.button
        )

        self.clicker.start()

        #---------------------------------------------------------------
        # Create GUI
        #---------------------------------------------------------------

        self.create_gui()

        #---------------------------------------------------------------
        # Keyboard Listener
        #---------------------------------------------------------------

        self.listener = Listener(
            on_press=self.on_press
        )

        self.listener.start()


    #===================================================================
    # GUI
    #===================================================================

    def create_gui(self):

        self.root.title("AutoClicker")
        self.root.attributes("-fullscreen", False)

        #---------------------------------------------------------------
        # Keyboard Bindings
        #---------------------------------------------------------------

        self.root.bind(
            "<Escape>",
            self.exit_fullscreen
        )

        self.root.bind(
            "<Control-q>",
            self.close_app
        )

        self.root.bind(
            "<Control-f>",
            self.enter_fullscreen
        )

        #---------------------------------------------------------------
        # Button Frame
        #---------------------------------------------------------------

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        exit_button = tk.Button(
            button_frame,
            text="Exit",
            command=self.close_app
        )

        exit_button.pack(
            side=tk.LEFT,
            padx=5
        )

        fullscreen_button = tk.Button(
            button_frame,
            text="Fullscreen",
            command=self.enter_fullscreen
        )

        fullscreen_button.pack(
            side=tk.LEFT,
            padx=5
        )

        #---------------------------------------------------------------
        # Instructions
        #---------------------------------------------------------------

        instructions = tk.Label(
            self.root,
            text=(
                "Press 'a' to start/stop clicking, "
                "'b' to exit, "
                "'Esc' to exit fullscreen, "
                "'Ctrl+F' to enter fullscreen, "
                "'Ctrl+Q' to quit."
            ),
            font=("Arial", 12)
        )

        instructions.pack(pady=20)

        #---------------------------------------------------------------
        # Configuration Frame
        #---------------------------------------------------------------

        config_frame = tk.Frame(self.root)
        config_frame.pack(pady=20)

        config_label = tk.Label(
            config_frame,
            text="Clicker Configuration",
            font=("Arial", 14, "bold")
        )

        config_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=10
        )

        #---------------------------------------------------------------
        # Start/Stop Key
        #---------------------------------------------------------------

        start_key_label = tk.Label(
            config_frame,
            text="Start/Stop Key:"
        )

        start_key_label.grid(
            row=1,
            column=0,
            sticky="e",
            padx=5
        )

        self.start_key_entry = tk.Entry(
            config_frame
        )

        self.start_key_entry.insert(
            0,
            self.start_key.char
        )

        self.start_key_entry.grid(
            row=1,
            column=1,
            padx=5
        )

        #---------------------------------------------------------------
        # Exit Key
        #---------------------------------------------------------------

        exit_key_label = tk.Label(
            config_frame,
            text="Exit Key:"
        )

        exit_key_label.grid(
            row=2,
            column=0,
            sticky="e",
            padx=5
        )

        self.exit_key_entry = tk.Entry(
            config_frame
        )

        self.exit_key_entry.insert(
            0,
            self.exit_key.char
        )

        self.exit_key_entry.grid(
            row=2,
            column=1,
            padx=5
        )

        #---------------------------------------------------------------
        # Mouse Button
        #---------------------------------------------------------------

        mouse_button_label = tk.Label(
            config_frame,
            text="Mouse Button:"
        )

        mouse_button_label.grid(
            row=3,
            column=0,
            sticky="e",
            padx=5
        )

        self.mouse_button_var = tk.StringVar(
            value="left"
        )

        mouse_button_menu = tk.OptionMenu(
            config_frame,
            self.mouse_button_var,
            "left",
            "right",
            "middle"
        )

        mouse_button_menu.grid(
            row=3,
            column=1,
            padx=5
        )

        #---------------------------------------------------------------
        # Delay
        #---------------------------------------------------------------

        delay_label = tk.Label(
            config_frame,
            text="Delay (seconds):"
        )

        delay_label.grid(
            row=4,
            column=0,
            sticky="e",
            padx=5
        )

        self.delay_entry = tk.Entry(
            config_frame
        )

        self.delay_entry.insert(
            0,
            str(self.delay)
        )

        self.delay_entry.grid(
            row=4,
            column=1,
            padx=5
        )

        #---------------------------------------------------------------
        # Apply Configuration
        #---------------------------------------------------------------

        apply_button = tk.Button(
            config_frame,
            text="Apply Configuration",
            command=self.apply_config
        )

        apply_button.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=15
        )


    #===================================================================
    # Keyboard Listener
    #===================================================================

    def on_press(self, key):

        if key == self.start_key:

            if self.clicker.click_event.is_set():

                self.clicker.stop_clicking()

                print("[INFO] Clicker Stopped.")

            else:

                self.clicker.start_clicking()

                print("[INFO] Clicker Started.")

        elif key == self.exit_key:

            self.close_app()


    #===================================================================
    # Configuration
    #===================================================================

    def apply_config(self):

        #---------------------------------------------------------------
        # Delay
        #---------------------------------------------------------------

        try:

            new_delay = float(
                self.delay_entry.get()
            )

            if new_delay < 0:
                raise ValueError

        except ValueError:

            print("[ERROR] Invalid delay.")

            return

        #---------------------------------------------------------------
        # Mouse Button
        #---------------------------------------------------------------

        button_name = self.mouse_button_var.get()

        button_map = {
            "left": Button.left,
            "right": Button.right,
            "middle": Button.middle
        }

        new_button = button_map.get(
            button_name
        )

        if new_button is None:

            print("[ERROR] Invalid mouse button.")

            return

        #---------------------------------------------------------------
        # Start/Stop Key
        #---------------------------------------------------------------

        start_key_value = (
            self.start_key_entry
            .get()
            .strip()
            .lower()
        )

        if len(start_key_value) != 1:

            print("[ERROR] Start/Stop key must be one character.")

            return

        new_start_key = KeyCode(
            char=start_key_value
        )

        #---------------------------------------------------------------
        # Exit Key
        #---------------------------------------------------------------

        exit_key_value = (
            self.exit_key_entry
            .get()
            .strip()
            .lower()
        )

        if len(exit_key_value) != 1:

            print("[ERROR] Exit key must be one character.")

            return

        new_exit_key = KeyCode(
            char=exit_key_value
        )

        #---------------------------------------------------------------
        # Apply
        #---------------------------------------------------------------

        self.delay = new_delay
        self.button = new_button
        self.start_key = new_start_key
        self.exit_key = new_exit_key

        self.clicker.update_config(
            delay=self.delay,
            button=self.button
        )

        print("[INFO] Configuration Applied.")


    #===================================================================
    # Fullscreen
    #===================================================================

    def exit_fullscreen(self, event=None):

        self.root.attributes(
            "-fullscreen",
            False
        )


    def enter_fullscreen(self, event=None):

        self.root.attributes(
            "-fullscreen",
            True
        )


    #===================================================================
    # Application Shutdown
    #===================================================================

    def close_app(self, event=None):

        print("[INFO] Exiting.")

        self.clicker.exit()

        if self.listener.is_alive():
            self.listener.stop()

        self.root.destroy()


#=======================================================================
# Main
#=======================================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = AutoClickerApp(root)

    root.mainloop()