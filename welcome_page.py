import tkinter as tk
import os

def proceed_button_click():
    # This function will be called when the "Proceed" button is clicked
    window.destroy()  # Close the current window
    os.system('python login_signup.py')  # Open the login and sign-up window

# Create the main window
window = tk.Tk()
window.title("Parking Management System")

# Create a label for the title
title_label = tk.Label(window, text="PARKING MANAGEMENT SYSTEM", font=("Helvetica", 16))
title_label.pack(pady=20)

# Create the "Proceed" button
proceed_button = tk.Button(window, text="Proceed", command=proceed_button_click)
proceed_button.pack()

# Start the GUI event loop for the main window
window.mainloop()
