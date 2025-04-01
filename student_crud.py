import psycopg2

def db_connection():
    DB_NAME = "postgres"
    USER = "postgres.klxuimqlrmasdugwilmk"
    PASSWORD = "Darshan@2064"
    host = "aws-0-ap-southeast-1.pooler.supabase.com"
    port = "6543"
    try:
        conn = psycopg2.connect(dbname = DB_NAME, user=USER,password=PASSWORD, host=host, port=port)
        return conn
    except Exception as e:
        print("Error in connection to the database")

def create_table():
    conn= db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully")

def insert_teacher(name,age,department_id):
    conn= db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teacher (name, age,department_id) VALUES (%s, %s,%s)", (name, age,department_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA INSERTED successfully")

def update_teacher(id,name,age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE teacher SET name = %s, age = %s WHERE id = %s",(name,age,id))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA UPDATED successfully")

def delete_teacher(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teacher where id = %s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA DELETED successfully")

def create_student_table():
    conn= db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        create table students (
            student_id serial primary key,
            name varchar(255),
            age INT,
            gender varchar(255),
            email varchar(255) unique
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully")

def create_course_table():
    conn= db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        create table courses (
            course_id int primary key,
            name text,
            description text,
            department_id int not null,
            credits int not null
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully")

def create_enrollment_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        create table enrollment (
            student_id int references students(student_id),
            course_id int references courses(course_id),
            teacher_id int references teacher(id),
            grade varchar(255)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully")

def insert_students(id,name,age,gender,email):
    conn= db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (student_id,name,age,gender,email) VALUES (%s, %s,%s,%s,%s)", (id,name, age, gender,email))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA INSERTED successfully")

def insert_courses(course_id,name,description,department_id,credits):
    conn= db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (course_id,name,description,department_id,credits) VALUES (%s, %s,%s,%s,%s)", (course_id,name, description, department_id, credits))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA INSERTED successfully")

def insert_enrollment(student_id,course_id,teacher_id,grade):
    conn= db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollment (student_id,course_id,teacher_id,grade) VALUES (%s, %s,%s,%s)", (student_id, course_id, teacher_id, grade))
    conn.commit()
    cursor.close()
    conn.close()
    print("DATA INSERTED successfully") 
    

if __name__ == "__main__":
    insert_enrollment(23101,101,4,12)

