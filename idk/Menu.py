import tkinter as tk
from tkinter import *
from tkinter import messagebox
login_window = tk.Tk()
login_window.title("Arisu")
login_window.geometry("800x600")
login_window.configure(bg="#97bcc7")




lgn_btn= tk.Button (login_window, text= "Login" ,font= ("Arial",13),width=30)
sgn_btn= tk.Button (login_window, text= "Sign Up" ,font= ("Arial",13),width=30)





lgn_btn.pack(pady=20)
sgn_btn.pack(pady=20)

 



login_window.mainloop()