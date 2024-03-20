import psycopg2

def connect(dtb, usr, hst, password, port):
    conn = psycopg2.connect(database = dtb, 
                            user = usr, 
                            host= hst,
                            password = password,
                            port = port)
    return conn

def getALLStudents(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM students;')
    rows = cur.fetchall()
    conn.commit()
    for row in rows:
        print(row)

def addStudent(conn,first_name, last_name, email, enrollment_date):
    cur = conn.cursor()
    cmd = "INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES(%s,%s,%s,%s);"
    cur.execute(cmd, (first_name,last_name,email,enrollment_date))
    conn.commit()
    cur.close()


def updateStudentEmail(conn, student_id, email):
    cur = conn.cursor()
    cmd = "UPDATE students SET email = %s WHERE student_id = %s"
    cur.execute(cmd, (email, student_id))
    conn.commit()
    cur.close()

def deleteStudent(conn, student_id):
    cur = conn.cursor()
    cmd = "DELETE from students WHERE student_id = %s"
    cur.execute(cmd, (student_id,))
    conn.commit()
    cur.close()
