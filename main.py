import pyotp
import time
import os
import tkinter as tk

def get_secret_key():
    secret_key = input("Enter the secret key: ")
    with open("secret.env", "w") as file:
        file.write(f"SECRET_KEY={secret_key}")

def update_totp():
    current_totp = totp.now()
    totp_label.config(text="Current TOTP: \n" + current_totp)  # Update the label with current TOTP
    window.after(1000, update_totp)  # Schedule the next update after 1 second

# Check if secret.env file exists
if os.path.isfile("secret.env"):
    with open("secret.env", "r") as file:
        secret_key = file.read().split("=")[1]
else:
    get_secret_key()
    with open("secret.env", "r") as file:
        secret_key = file.read().split("=")[1]

totp = pyotp.TOTP(secret_key)

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
