import tkinter as tk

def parent_window():
    win = tk.Toplevel()
    win.title("Parent Form")
    win.geometry("300x300")

    tk.Label(win, text="Parent Name").pack()
    tk.Entry(win).pack()

    tk.Label(win, text="Student ID").pack()
    tk.Entry(win).pack()

    tk.Label(win, text="Contact Number").pack()
    tk.Entry(win).pack()
    
    tk.Button(win, text="Save Parent", bg="orange", fg="white").pack(pady=10)
