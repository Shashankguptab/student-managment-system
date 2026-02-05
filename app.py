import mysql.connector

# database connection
conn = mysql.connector.connect(
    host="localhost", user="root", password="Royal@580", database="student_db"
)

cursor = conn.cursor()

# create table
cursor.execute(
    """
create table if not exists students (
    id int auto_increment primary key,
    name varchar(50),
    age int,
    course varchar(50)
)"""
)


# insert student
def add_student(name, age, course):
    query = "insert into students (name, age, course) values (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    conn.commit()
    print("student added successfully")


# view students
def view_students():
    cursor.execute("select * from students")
    data = cursor.fetchall()
    for row in data:
        print(row)


# main
while True:
    print("\n1. add student")
    print("2. view students")
    print("3. exit")

    choice = input("enter choice: ")

    if choice == "1":
        name = input("enter name: ")
        age = int(input("enter age: "))
        course = input("enter course: ")
        add_student(name, age, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        break

    else:
        print("invalid choice")

conn.close()
