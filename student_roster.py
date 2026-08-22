import sqlite3

connection = sqlite3.connect('school.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        gpa REAL NOT NULL,
        grade TEXT NOT NULL
    )
""")

def add_student(name, gpa, grade):
    cursor.execute(
        "INSERT INTO students (name, gpa, grade) VALUES (?, ?, ?)", 
        (name, gpa, grade)
    )
    connection.commit()

students_names = [
        ("Amy", 3.9, "A"),
        ("Bob", 3.7, "B"),
        ("Charlie", 4.0, "A"),
        ("David", 3.5, "C"),

]




cursor.execute("SELECT * FROM students")

#print("=== Students ===")

#for student in cursor.fetchall():
    #print(student)


def get_all_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def get_student_by_id(student_id):
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    return cursor.fetchone()
    connection.commit()

get_all_students()


def update_student_gpa(student_id, new_gpa):
    cursor.execute("UPDATE students SET gpa = 3.6 WHERE id = 2") 
    connection.commit()

update_student_gpa(2, 3.6)

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()


delete_student(1)

cursor.execute("SELECT * FROM students")

print("=== Students ===")

for student in cursor.fetchall():
    print(student)

  



    