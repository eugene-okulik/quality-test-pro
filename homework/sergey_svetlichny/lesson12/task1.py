# Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
#
# Создайте студента (student)
# Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
# Создайте группу (group) и определите своего студента туда
# Создайте несколько учебных предметов (subjects)
# Создайте по два занятия для каждого предмета (lessons)
# Поставьте своему студенту оценки (marks) для всех созданных вами занятий
# Получите информацию из базы данных:
#
# Все оценки студента
# Все книги, которые находятся у студента
# Если разберетесь с Join, то вот еще (это дополнительное задание - можно вообще не выполнять, можно выполнить только
# что-то одно, а можно и всё):
#
# При получении всех оценок, для каждой оценки получите название предмета (в одном запросе)
# Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (тоже
# одним запросом)

import mysql.connector as mysql

db = mysql.connect(

    user='qtp',
    passwd='AVNS_N3ClDVXuh4feLZCN60R',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qtp'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (id, name, second_name, group_id) VALUES (NULL, 'Tom', 'Soyer', NULL)")
db.commit()
student_id = cursor.lastrowid
print(student_id)

cursor.execute(f"INSERT INTO books (id, title, taken_by_student_id) VALUES (NULL, 'Kak dostat babulyu', {student_id})")
cursor.execute(f"INSERT INTO books (id, title, taken_by_student_id) VALUES (NULL, 'Pokraska zabora dla chainikov',"
               f" {student_id})")
cursor.execute("INSERT INTO `groups` (id, title, start_date, end_date) "
               + "VALUES (NULL, 'Maliary', '1 Sep 2023' , '15 Sep 2023') ")
db.commit()
group_id = cursor.lastrowid
# print(group_id)

cursor.execute(f"UPDATE students SET group_id  = {group_id} where id = {student_id}")

cursor.execute("INSERT INTO `subjets` (id, title) VALUES (NULL, 'Maths')")
db.commit()
math_id = cursor.lastrowid
cursor.execute("INSERT INTO `subjets` (id, title) VALUES (NULL, 'Physics')")
db.commit()
physics_id = cursor.lastrowid

cursor.execute(f"INSERT INTO `lessons` (id, title, subject_id) VALUES (NULL, 'Algebra', {math_id})")
db.commit()
algebra_id = cursor.lastrowid
cursor.execute(f"INSERT INTO `lessons` (id, title, subject_id) VALUES (NULL, 'Geometry', {math_id})")
db.commit()
geometry_id = cursor.lastrowid
cursor.execute(f"INSERT INTO `lessons` (id, title, subject_id) VALUES (NULL, 'Physics of Metals', {physics_id})")
db.commit()
phys_met_id = cursor.lastrowid
cursor.execute(f"INSERT INTO `lessons` (id, title, subject_id) VALUES (NULL, 'Physics of Water', {physics_id})")
db.commit()
phys_wat_id = cursor.lastrowid

cursor.execute(f"INSERT INTO `marks` (id, value, lesson_id, student_id) VALUES (NULL, 4, {algebra_id}, {student_id})")
cursor.execute(f"INSERT INTO `marks` (id, value, lesson_id, student_id) VALUES (NULL, 5, {geometry_id}, {student_id})")
cursor.execute(f"INSERT INTO `marks` (id, value, lesson_id, student_id) VALUES (NULL, 3, {phys_met_id}, {student_id})")
cursor.execute(f"INSERT INTO `marks` (id, value, lesson_id, student_id) VALUES (NULL, 3, {phys_wat_id}, {student_id})")

db.commit()

cursor.execute(f'SELECT title as Lesson, value as Mark FROM lessons l '
               f'JOIN marks m '
               f'ON l.id = m.lesson_id where student_id = {student_id}')
result = cursor.fetchall()
print(result)

cursor.execute(f'SELECT title as NameBook FROM books where taken_by_student_id = {student_id}')
result = cursor.fetchall()
print(result)

cursor.execute("SELECT name, second_name, b.title as bookname, g.id as group_number, g.title as group_title, "
               "m.value as mark, l.title as lesson FROM students s "
               "JOIN books b "
               "ON s.id = b.taken_by_student_id "
               "JOIN `groups` g "
               "ON s.group_id = g.id "
               "JOIN marks m "
               "ON s.id = m.student_id "
               "JOIN lessons l "
               "ON l.id = m.lesson_id "
               f"where s.id = {student_id}")

result = cursor.fetchall()
print(result)

db.close()
