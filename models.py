import hashlib
import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

def create_database():
    StudentsTB='''
    CREATE TABLE IF NOT EXISTS Students(
        StudentID INTEGER PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        email VARCHAR(20),
        password VARCHAR(32)
    )
    '''
    LecturersTB='''
    CREATE TABLE IF NOT EXISTS Lecturers(
        LecturerID INTEGER PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        email VARCHAR(20),
        password VARCHAR(32)
    )
    '''
    AdminsTB='''
    CREATE TABLE IF NOT EXISTS Admins(
        AdminID INTEGER PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        email VARCHAR(20),
        password VARCHAR(32)
    )
    '''
    cur.execute(StudentsTB)
    cur.execute(LecturersTB)
    cur.execute(AdminsTB)

    students_sql_query = "INSERT OR IGNORE INTO Students (StudentID,first_name,last_name,email,password) VALUES (?, ?, ?, ?, ?)"

    lecturers_sql_query = "INSERT OR IGNORE INTO Lecturers (LecturerID,first_name,last_name,email,password) VALUES (?, ?, ?, ?, ?)"

    admins_sql_query = "INSERT OR IGNORE INTO Admins (AdminID,first_name,last_name,email,password) VALUES (?, ?, ?, ?, ?)"
    default_pass = b'1234'
    val = [
        ("1","Frederick","Omondi","frankomondi311@gmail.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("2","Dofften","Dofften","dofften@dofften.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("3","Omondi","Kiilu","omondi@kiilu.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("4","Kamau","Kamau","kamau@kamau.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("5","Aketch","Aketch","aketch@aketch.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("6","Mirugi","Mirugi","mirugi@mirugi.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("7","Kibet","Kibet","kibet@kibet.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("8","Kioko","Kioko","kioko@kioko.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("9","Kinyua","Kinyua","kinyua@kinyua.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("10","Nandasaba","Nandasaba","nandasaba@nandasaba.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("11","John","Doe","johndoe@johndoe.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("12","Bryan","Gil","bryangil@bryangil.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("13","Cristiano","Ronaldo","ronaldo@ronaldo.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("14","Mikel","Arteta","nandasaba@nandasaba.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("15","Lionel","Messi","messi@messi.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("16","nandasaba","nandasaba","nandasaba@nandasaba.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("17","Victoria","Atieno","vicky@vicky.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("18","Sean","Onalo","sean@sean.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("19","Jake","Peralta","jake@jake.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("20","Amy","Santiago","amy@amy.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
        ("21","CUEA","CUEA","cuea@cuea.com",f"{hashlib.sha256(default_pass).hexdigest()}"),
    ]

    cur.executemany(students_sql_query, val)
    cur.executemany(lecturers_sql_query, val)
    cur.executemany(admins_sql_query, val)


    # cur.execute("SELECT * FROM Students")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)
    conn.commit()
    cur.close()

    conn.close()


# create_database()