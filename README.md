# School Management System (Python + Tkinter + MySQL)

## 📌 Project Overview

Ye project **School Management System** ka basic version hai jisme **GUI (Graphical User Interface)** ke through school-related data easily manage kiya ja sakta hai. Is system me user bina SQL likhe **Students ka data form ke through MySQL database me store** kar sakta hai.

Project ka main focus:

* User-friendly GUI
* Python + Tkinter ka use
* MySQL Workbench ke saath proper database connectivity
* Beginner + College Project friendly structure

---

## 🧰 Technologies Used

* **Python 3.x**
* **Tkinter** (GUI ke liye)
* **MySQL Server & MySQL Workbench**
* **mysql-connector-python** (Python–MySQL connectivity)
* **VS Code** (Recommended IDE)

---

## 📂 Project Folder Structure

```
School_Project/
│
├── main.py          # Main menu (Students / Teachers / Parents)
├── student.py       # Student GUI + Database Insert Logic
├── teacher.py       # (Future use)
├── parent.py        # (Future use)
├── db_config.py     # MySQL Database Connection File
└── README.md        # Project Documentation
```

---

## 🗄️ Database Details

### Database Name

```
SCHOOL
```

### Students Table Structure

```sql
CREATE TABLE students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    RollNo INT,
    Gender VARCHAR(10),
    Dob DATE,
    City VARCHAR(50)
);
```

---

## ⚙️ Setup Instructions (Step-by-Step)

### 1️⃣ Python Install Check

```bash
python --version
```

### 2️⃣ MySQL Connector Install

```bash
pip install mysql-connector-python
```

### 3️⃣ Database Connection Setup

`db_config.py` file me apna MySQL password set karein:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="SCHOOL"
    )
```

---

## ▶️ How to Run the Project

1. VS Code me project folder open karein
2. Terminal open karein
3. Run command execute karein:

```bash
python main.py
```

4. Main GUI open hoga
5. **Students** option select karein
6. Form fill karke **Save Student** button click karein
7. Data MySQL database me store ho jayega

---

## ✅ Features Implemented

* Main Menu GUI
* Student Data Entry Form
* MySQL Database Connectivity
* Error Handling (try–except)
* Clean & Modular Code Structure

---

## 🚀 Future Enhancements

* Teacher & Parent modules
* Update / Delete student records
* Search functionality
* Login system (Admin / User)
* Single-window (Frame based) GUI

---

## 🎓 Viva / Explanation Line

> “Is project me maine Python Tkinter ka use karke GUI banaya hai jo MySQL database se connected hai. User form ke through student data enter karta hai jo directly database me save hota hai.”

---

## 👨‍💻 Developed By

**Rahul Verma**
Engineering Student – Computer Science

---

✅ *Ye project beginners ke liye best hai jo Python, GUI aur MySQL integration seekhna chahte hain.*

