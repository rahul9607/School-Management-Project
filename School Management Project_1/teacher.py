import tkinter as tk

def teacher_window():
    win = tk.Toplevel()
    win.title("Teacher Form")
    win.geometry("300x300")

    tk.Label(win, text="Teacher ID").pack()
    tk.Entry(win).pack()

    tk.Label(win, text="Name").pack()
    tk.Entry(win).pack()

    tk.Label(win, text="Subject Name").pack()
    tk.Entry(win).pack()
    
    tk.Label(win, text="Contact Number").pack()
    tk.Entry(win).pack()

    tk.Button(win, text="Save Teacher", bg="blue", fg="white").pack(pady=10)
