import tkinter as tk
from Student import student_window
from teacher import teacher_window
from parents import parent_window

root = tk.Tk()
root.title("School Management System")
root.geometry("300x300")

tk.Label(root, text="Select Module", font=("Arial", 14, "bold")).pack(pady=20)

tk.Button(root, text="STUDENTS", width=20, command=student_window).pack(pady=5)
tk.Button(root, text="TEACHERS", width=20, command=teacher_window).pack(pady=5)
tk.Button(root, text="PARENTS", width=20, command=parent_window).pack(pady=5)

root.mainloop()
