import tkinter as tk
import os

def signup():
    # This function will be called when the "Sign Up" button is clicked
    print("Sign Up functionality goes here")
def back_b():
    signup_window.destroy()
    os.system('python login_signup.py')

# Create the signup window
signup_window = tk.Tk()
signup_window.title("Sign Up")

# Create a label for the signup page
signup_label = tk.Label(signup_window, text="Sign Up Page", font=("Helvetica", 16))
signup_label.pack(pady=20)

# Create the "Sign Up" button
signup_button = tk.Button(signup_window, text="Sign Up", command=signup)
signup_button.pack()

#create Back Button
back_b_button = tk.Button(signup_window, text="Back", command=back_b)
back_b_button.pack()


# Start the GUI event loop for the signup window
signup_window.mainloop()
