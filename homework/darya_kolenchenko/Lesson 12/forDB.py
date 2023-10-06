import mysql.connector as mysql

db = mysql.connect(
    user='qtp',
    passwd='AVNS_N3ClDVXuh4feLZCN60R',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qtp'
)

cursor = db.cursor(dictionary=True)

# #  insert student
# query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
# values = ('Ron', 'Weasley')
# cursor.execute(query, values)
# cursor.execute('SELECT * FROM students')
# student_id = cursor.lastrowid
# print(cursor.fetchall())
#
#
# #  insert books
# query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
# values = [
#     ('Dark charms', '24'),
#     ('Forecasting', '24')
#     ]
# cursor.executemany(query, values)
# cursor.execute('SELECT * FROM books')
# print(cursor.fetchall())
#
#
# #  insert group
# query = 'INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
# values = ('Gryffindor', '20-07-2010', '20-09-2024')
# cursor.execute(query, values)
# cursor.execute('SELECT * FROM `groups`')
# print(cursor.fetchall())
#
#
# #  update students with group_id
# cursor.execute('UPDATE students SET group_id = 12 WHERE id = 24')
# cursor.execute('SELECT * FROM students')
# print(cursor.fetchall())
#
#
# #  insert subjects
# query = 'INSERT INTO subjets (title) VALUE (%s)'
# values = [
#     ('Chanting',),
#     ('Shamans',)
#     ]
# cursor.executemany(query, values)
# cursor.execute('SELECT * FROM subjets')
# print(cursor.fetchall())
#
#
# #  insert lessons
# query = 'INSERT INTO lessons (title, subject_id) VALUE (%s, %s)'
# values = [
#     ('chanting', '11'),
#     ('Shamaning', '12'),
# ]
# cursor.executemany(query, values)
# cursor.execute('SELECT * FROM lessons')
# print(cursor.fetchall())
#
#
#  insert marks
# query = 'INSERT INTO marks (value, lesson_id, student_id) VALUE (%s, %s, %s)'
# values = [
#     ('4', '19', '24'),
#     ('6', '20', '24'),
#     ('10', '4', '24'),
#     ('7', '5', '24')
# ]
# cursor.executemany(query, values)
# cursor.execute('SELECT * FROM marks')
# print(cursor.fetchall())
#
#
#  get all student's marks
cursor.execute('SELECT * FROM marks where student_id = 24')
print(cursor.fetchall())


#  get all student's books
cursor.execute('SELECT * FROM books where taken_by_student_id = 24')
print(cursor.fetchall())
#
#
#  get all student's marks with subjects
cursor.execute('SELECT marks.value, subjets.title FROM marks '
               'JOIN lessons ON marks.lesson_id=lessons.id '
               'JOIN subjets ON lessons.subject_id = subjets.id where student_id = 24')
print(cursor.fetchall())

db.commit()
db.close()
