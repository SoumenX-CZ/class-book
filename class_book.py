import sqlite3
import tkinter as tk
from tkinter import ttk

# Připojení k databázi
conn = sqlite3.connect("tridni_kniha.db")
cursor = conn.cursor()

# Vytvoření tabulky studentů
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    jmeno TEXT)""")

# Vytvoření tabulky docházky
cursor.execute("""CREATE TABLE IF NOT EXISTS attendance (
                    student_id INTEGER,
                    date TEXT,
                    status TEXT,
                    FOREIGN KEY(student_id) REFERENCES students(id))""")
conn.commit()

# Funkce pro přidání studenta
def add_student():
    jmeno = entry_student.get()
    if jmeno:
        cursor.execute("INSERT INTO students (jmeno) VALUES (?)", (jmeno,))
        conn.commit()
        update_students()
        entry_student.delete(0, tk.END)

# Aktualizace seznamu studentů
def update_students():
    listbox_students.delete(0, tk.END)
    cursor.execute("SELECT * FROM students")
    for student in cursor.fetchall():
        listbox_students.insert(tk.END, student)

# Zápis docházky
def record_attendance():
    selected = listbox_students.curselection()
    if selected:
        student_id = listbox_students.get(selected[0])[0]
        date = entry_date.get()
        status = status_var.get()
        cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)", (student_id, date, status))
        conn.commit()

# GUI
root = tk.Tk()
root.title("Třídní kniha")

# Sekce pro přidání studenta
frame_top = tk.Frame(root)
frame_top.pack()

tk.Label(frame_top, text="Jméno studenta:").pack(side=tk.LEFT)
entry_student = tk.Entry(frame_top)
entry_student.pack(side=tk.LEFT)
tk.Button(frame_top, text="Přidat", command=add_student).pack(side=tk.LEFT)

# Seznam studentů
listbox_students = tk.Listbox(root)
listbox_students.pack()
update_students()

# Sekce pro docházku
frame_bottom = tk.Frame(root)
frame_bottom.pack()

tk.Label(frame_bottom, text="Datum (YYYY-MM-DD):").pack(side=tk.LEFT)
entry_date = tk.Entry(frame_bottom)
entry_date.pack(side=tk.LEFT)

status_var = tk.StringVar(value="Přítomen")
ttk.Combobox(frame_bottom, textvariable=status_var, values=["Přítomen", "Nepřítomen"]).pack(side=tk.LEFT)
tk.Button(frame_bottom, text="Zapsat docházku", command=record_attendance).pack(side=tk.LEFT)

root.mainloop()