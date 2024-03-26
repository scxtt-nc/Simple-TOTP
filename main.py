import pyotp
import time
import os

totp = pyotp.TOTP("")

password = input("Enter password: ")
if password == "":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
        print("Current TOTP:", totp.now())
        time.sleep(30)
else:
    print("Incorrect password. Access denied.")
