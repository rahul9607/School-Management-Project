import tkinter as tk
from tkinter import messagebox
from db_config import get_connection

def student_window():
    win = tk.Toplevel()
    win.title("Student Form")
    win.geometry("350x420")

    tk.Label(win, text="Student ID").pack()
    entry_id = tk.Entry(win)
    entry_id.pack()

    tk.Label(win, text="Student Name").pack()
    entry_name = tk.Entry(win)
    entry_name.pack()

    # add student Class fields
    tk.Label(win, text="Class").pack()
    entry_class = tk.Entry(win)
    entry_class.pack()

    tk.Label(win, text="Roll Number").pack()
    entry_roll = tk.Entry(win)
    entry_roll.pack()

    tk.Label(win, text="Gender").pack()
    entry_gender = tk.Entry(win)
    entry_gender.pack()

    tk.Label(win, text="Date of Birth (YYYY-MM-DD)").pack()
    entry_dob = tk.Entry(win)
    entry_dob.pack()

    tk.Label(win, text="City").pack()
    entry_city = tk.Entry(win)
    entry_city.pack()

    def save_student():
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO students
            (StudentID, StudentName, RollNo, Gender, Dob, City)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            data = (
                entry_id.get(),
                entry_name.get(),
                entry_class.get(),
                entry_roll.get(),
                entry_gender.get(),
                entry_dob.get(),
                entry_city.get()
            )

            cursor.execute(query, data)
            conn.commit()

            messagebox.showinfo("Success", "Student Saved Successfully")

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        win,
        text="Save Student",
        bg="green",
        fg="white",
        command=save_student
    ).pack(pady=10)
