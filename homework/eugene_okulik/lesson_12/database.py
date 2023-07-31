import mysql.connector as mysql

db = mysql.connect(
    user='qtp',
    passwd='AVNS_N3ClDVXuh4feLZCN60R',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='qtp'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('SELECT * FROM students')
# student_id = input('enter sudent id: ')
# query = "SELECT * FROM students WHERE id = %s and name = 'James'"
# values = (student_id,)
# cursor.execute(query, values)

cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Python for dummies', NULL)")
db.commit()
book_id = cursor.lastrowid

# result = cursor.fetchone()
# print(result['name'])
print(book_id)

db.close()
