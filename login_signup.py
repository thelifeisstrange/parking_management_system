import tkinter as tk
import os

def open_login_page():
    # This function will be called when the "Login" button is clicked
    menu_window.destroy()
    os.system('python login_page.py')  # Open the login page

def open_signup_page():
    # This function will be called when the "Sign Up" button is clicked
    menu_window.destroy()
    os.system('python signup_page.py')  # Open the signup page

# Create the menu window
menu_window = tk.Tk()
menu_window.title("Menu")

# Create a label for "Already a user?"
already_user_label = tk.Label(menu_window, text="Already a user?", font=("Helvetica", 16))
already_user_label.pack(pady=10)

# Create the "Login" button
login_button = tk.Button(menu_window, text="Login", command=open_login_page)
login_button.pack()

# Create a label for "New here?"
new_here_label = tk.Label(menu_window, text="New here?", font=("Helvetica", 16))
new_here_label.pack(pady=10)

# Create the "Sign Up" button
signup_button = tk.Button(menu_window, text="Sign Up", command=open_signup_page)
signup_button.pack()

# Start the GUI event loop for the menu window
menu_window.mainloop()
