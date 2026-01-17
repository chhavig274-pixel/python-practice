import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="password",
    database="school"   
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    branch VARCHAR(50)
)
""")

def add_student(name, age, branch):
    query = "INSERT INTO students (name, age, branch) VALUES (%s, %s, %s)"
    values = (name, age, branch)
    cursor.execute(query, values)
    conn.commit()

def show_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def update_branch(student_id, new_branch):
    query = "UPDATE students SET branch = %s WHERE id = %s"
    cursor.execute(query, (new_branch, student_id))
    conn.commit()

def delete_student(student_id):
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

add_student("Chhavi", 19, "CSE")
add_student("Aman", 20, "ECE")

show_students()

update_branch(1, "AI & DS")
delete_student(2)

show_students()

cursor.close()
conn.close()
