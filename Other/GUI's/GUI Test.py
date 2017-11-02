#Imports
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create instance
win = tk.Tk()

# Add a title
win.title("Change password")

# username
ttk.Label(win, text="Username:").grid(column=1, row=1)
username = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=username)
nameEntered.grid(column=2, row=1, padx=10, pady=10)
# password
ttk.Label(win, text="New password:").grid(column=1, row=2)
password = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=password)
nameEntered.grid(column=2, row=2, padx=10, pady=10)
password = password.get()
# confirm password
ttk.Label(win, text="Confirm password:").grid(column=1, row=3)
confirm_password = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=confirm_password)
nameEntered.grid(column=2, row=3, padx=10, pady=10)
confirm_password = confirm_password.get()
# button click
def clickMe():
    messagebox.showinfo('Information Message Box', 'Hello, ' + username + \
                        ', your new password is: ' + password)

# confirm button
action = ttk.Button(win, text="Change Password", command = clickMe)
action.grid(column=4, row=5, padx=20, pady=20)

# Start GUI
win.mainloop()