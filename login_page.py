import tkinter as tk
import os

def login():
    # This function will be called when the "Login" button is clicked
    print("Login functionality goes here")

def back_a():
    login_window.destroy()
    os.system('python login_signup.py')

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Create a label for the login page
login_label = tk.Label(login_window, text="Login Page", font=("Helvetica", 16))
login_label.pack(pady=20)

# Create the "Login" button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

#create Back Button
back_a_button = tk.Button(login_window, text="Back", command=back_a)
back_a_button.pack()

# Start the GUI event loop for the login window
login_window.mainloop()
