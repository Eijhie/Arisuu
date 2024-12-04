import tkinter as tk
from tkinter import ttk

def login():
    username = email_label.get()
    password = password_label.get()

    if username






# Create the main window
window = tk.Tk()
window.title("Arisu Inventory System")
window.configure(bg="#97bcc7")  # Light blue background
window.geometry("800x600")  # Set window size to 800x600 pixels


# Create the logo frame
logo_frame = tk.Frame(window, bg="#C0D6E4")
logo_frame.pack(pady=20)

# Add a placeholder for the logo (you'll need to replace this with your actual logo)
logo_label = tk.Label(logo_frame, text="ARISU INVENTORY SYSTEM", font=("Arial", 24), bg="#C0D6E4")
logo_label.pack(pady=20)

# Create the email field
username = tk.Label(window, text="Email:", font=("Arial", 14), bg="#C0D6E4")
username.pack(pady=10)
username_entry = tk.Entry(window, font=("Arial", 14), width=30)
email_entry.pack(pady=10)

# Create the password field
password_label = tk.Label(window, text="Password:", font=("Arial", 14), bg="#C0D6E4")
password_label.pack(pady=10)
password_entry = tk.Entry(window, show="*", font=("Arial", 14), width=30)
password_entry.pack(pady=10)

# Create the login button
login_button = tk.Button(window, text="Log In", font=("Arial", 14), command=lambda: print("Login button clicked!"))
login_button.pack(pady=10)

# Create the "Dont have an account" link
create_account_label = tk.Label(window, text="Dont have an account", font=("Arial", 12), bg="#C0D6E4")
create_account_label.pack(pady=10)

# Start the main loop
window.mainloop()