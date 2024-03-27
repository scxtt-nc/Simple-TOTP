import pyotp
import time
import os
import tkinter as tk

totp = pyotp.TOTP("secret key")

def check_password():
    password = password_entry.get()
    if password == "password here":
        def update_totp():
            current_totp = totp.now()
            totp_label.config(text="Current TOTP: \n" + current_totp)  # Update the label with current TOTP
            password_label.pack_forget()  # Hide the password label
            password_entry.pack_forget()  # Hide the password entry
            submit_button.pack_forget()
            window.after(1000, update_totp)  # Schedule the next update after 1 seconds

        update_totp()  # Start the initial update
        access_label.config(text="")  # Clear the access label
    else:
        access_label.config(text="Incorrect password. Access denied.")

# Create the main window
window = tk.Tk()
window.title("TOTP GUI")

# Set window size to match screen resolution
window.resizable(False, False)
screen_width = 256
screen_height = 128
window.geometry(f"{screen_width}x{screen_height}")

# Create password label and entry
password_label = tk.Label(window, text="Enter password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create access label
access_label = tk.Label(window, text="")
access_label.pack()

# Create TOTP label
totp_label = tk.Label(window, text="", font=("Segoe UI", 20))
totp_label.pack()

# Create submit button
submit_button = tk.Button(window, text="Submit", command=check_password)
submit_button.pack()

# Start the GUI event loop
window.mainloop()
