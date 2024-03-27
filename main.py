import pyotp
import time
import os
import tkinter as tk

totp = pyotp.TOTP("secret key")

def update_totp():
    current_totp = totp.now()
    totp_label.config(text="Current TOTP: \n" + current_totp)  # Update the label with current TOTP
    window.after(1000, update_totp)  # Schedule the next update after 1 second

# Create the main window
window = tk.Tk()
window.title("TOTP GUI")

# Set window size to match screen resolution
window.resizable(False, False)
screen_width = 256
screen_height = 128
window.geometry(f"{screen_width}x{screen_height}")

# Create TOTP label
totp_label = tk.Label(window, text="", font=("Segoe UI", 20), justify="center")
totp_label.pack()

# Start the initial update
update_totp()

# Start the GUI event loop
window.mainloop()
