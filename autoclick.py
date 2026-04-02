#=======================================================================
# Auto Clicker Macro
# This script will continuously click at the current mouse position
# until you stop it by pressing a predefined key
#
# Author: Gavin Childers
# Date: 2026-04-01
# Last Updated: 2026-04-01
#
# Version 1.0.0 - Basic Functionality, UI, and OBS Overlay
#=======================================================================

# Imports
import tkinter as tk
from tkinter import ttk
import threading
import time
import pyautogui
from pynput import keyboard

# Global States
running = False

# Click Loop
def click_loop(cps):
    global running
    delay = 1 / cps

    while running:
        pyautogui.click()
        time.sleep(delay)

# Pre-Timer + Start Logic
def pre_timer_and_start(cps, duration):
    global running

    remaining = duration

    # Show overlay
    overlay.deiconify()

    while remaining > 0:
        overlay_label.config(text=f"Starting in {remaining}")
        time.sleep(1)
        remaining -= 1

    # Hide overlay
    #overlay.withdraw()

    # Start clicking
    running = True
    threading.Thread(
        target=click_loop,
        args=(cps,),
        daemon=True
    ).start()

# Start / Stop
def start_clicking():
    global running

    if running:
        return

    cps = float(cps_slider.get())
    duration = int(timer_slider.get())

    threading.Thread(
        target=pre_timer_and_start,
        args=(cps, duration),
        daemon=True
    ).start()


def stop_clicking():
    global running
    running = False
    overlay.withdraw()

# Key Listener (F6 Toggle)
def on_press(key):
    global running
    try:
        if key == keyboard.Key.f6:
            if running:
                stop_clicking()
            else:
                start_clicking()
    except:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

# UI Setup
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x300")

# CPS Label
cps_label = ttk.Label(root, text="Clicks Per Second")
cps_label.pack()

# CPS Slider
cps_slider = ttk.Scale(root, from_=1, to=50, orient="horizontal")
cps_slider.set(10)
cps_slider.pack()

cps_value_label = ttk.Label(root, text="10 CPS")
cps_value_label.pack()

# Timer Label
timer_label = ttk.Label(root, text="Start Delay (seconds)")
timer_label.pack()

# Timer Slider
timer_slider = ttk.Scale(root, from_=1, to=300, orient="horizontal")
timer_slider.set(5)
timer_slider.pack()

timer_value_label = ttk.Label(root, text="5 sec")
timer_value_label.pack()

# Dynamic Slider Updates
def update_cps(val):
    cps_value_label.config(text=f"{int(float(val))} CPS")

def update_timer(val):
    timer_value_label.config(text=f"{int(float(val))} sec")

cps_slider.config(command=update_cps)
timer_slider.config(command=update_timer)

# Buttons
start_btn = ttk.Button(root, text="Start", command=start_clicking)
start_btn.pack(pady=5)

stop_btn = ttk.Button(root, text="Stop", command=stop_clicking)
stop_btn.pack(pady=5)

# Overlay Window (OBS Ready)
overlay = tk.Toplevel(root)
overlay.overrideredirect(True)
overlay.attributes("-topmost", True)

# OBS-specific: give title and transparency
overlay.title("ClickerOverlay")
overlay.config(bg="black")
overlay.attributes("-transparentcolor", "black")

# Center overlay on screen
overlay.update_idletasks()
width = 250
height = 100
screen_width = overlay.winfo_screenwidth()
screen_height = overlay.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
overlay.geometry(f"{width}x{height}+{x}+{y}")

# Overlay label
overlay_label = tk.Label(
    overlay,
    text="",
    font=("Arial", 24, "bold"),
    bg="black",
    fg="white"
)
overlay_label.pack(fill="both", expand=True)

# Hide initially
overlay.withdraw()

# Make overlay draggable
def start_move(event):
    overlay.x = event.x
    overlay.y = event.y

def do_move(event):
    x = event.x_root - overlay.x
    y = event.y_root - overlay.y
    overlay.geometry(f"+{x}+{y}")

overlay.bind("<Button-1>", start_move)
overlay.bind("<B1-Motion>", do_move)

# ======================
#        MAIN
# ======================
root.mainloop()
