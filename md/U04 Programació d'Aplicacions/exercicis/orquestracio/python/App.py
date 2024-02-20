import mysql.connector

connection = mysql.connector.connect(
    user='root', password='toor', host='db', port="3306", database='alumnes')
print("DB connected")

cursor = connection.cursor()

def show_students():
    
    # Execute the query
    cursor.execute('SELECT * FROM students')

    # Fetch the results
    students = cursor.fetchall()

    # Print the results
    for student in students:
        print(student)


show_students()


connection.close()