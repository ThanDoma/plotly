import psycopg2

#Подключение к таблице
con = psycopg2.connect(
  database='postgres',
  user='postgres',
  password='12345',
  host='127.0.0.1',
  port='5432'
)

print('Database opened successfully')
cur = con.cursor()


"""Создание таблицы (при повторном запуске выдаст ошибку отношения)

cur.execute('''CREATE TABLE students
               (ADMISSION INT PRIMARY KEY NOT NULL,
               NAME TEXT NOT NULL,
               AGE INT NOT NULL,
               COURSE CHAR(50),
               DEPARTMENT CHAR(50));''')
print("Table created successfully")"""


"""Вставка данных (Ключи не должны совпадать, иначе будет выдана ошибка )

cur.execute(
    "INSERT INTO STUDENTS (ADMISSION, NAME, AGE, COURSE, DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT') "
)
cur.execute(
    "INSERT INTO STUDENTS (ADMISSION, NAME, AGE, COURSE, DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT') "
)
cur.execute(
    "INSERT INTO STUDENTS (ADMISSION, NAME, AGE, COURSE, DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering') "
)
cur.execute(
    "INSERT INTO STUDENTS (ADMISSION, NAME, AGE, COURSE, DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT') "
)
print("Record inserted successfully")

#помогает применить изменения, внесенные в таблицу
con.commit()"""

"""
Вывод данных из таблицы
Будут выведены все данные 

cur.execute("SELECT admission, name, age, course, department from STUDENTS")

rows = cur.fetchall()
for row in rows:
    print('ADMISSION = ', row[0])
    print('NAME = ', row[1])
    print('AGE = ', row[2])
    print('COURSE = ', row[3])
    print('DEPARTMENT = ', row[4], '\n')

print('Operation done successfully')"""

'''Обновление таблиц
cur.execute("UPDATE STUDENTS set AGE = 20 where ADMISSION = 3420")
con.commit()

cur.execute('SELECT admission, age, name, course, department from STUDENTS')

rows = cur.fetchall()
for row in rows:
    print('ADMISSION =',row[0])
    print('NAME', row[1])
    print('AGE', row[2])
    print('COURSE', row[3])
    print('DEPARTMENT', row[4], '\n')

print("Operation done successfully")'''

'''Удаление строк
cur = con.cursor()
cur.execute("DELETE from STUDENTS where ADMISSION=3420;")
con.commit()'''

con.close()