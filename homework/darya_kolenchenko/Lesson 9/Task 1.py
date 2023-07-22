class Book:
    pages_material = 'бумага'
    text = True

    def __init__(self, title, author, num_pages, isbn, booked):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.ISBN = isbn
        self.booked = booked

    def __str__(self):
        if self.booked:
            return f'Название: {self.title}; Автор: {self.author}; страниц: {self.num_pages}; зарезервирована'
        return f'Название: {self.title}; Автор: {self.author}; страниц: {self.num_pages};'


book_1 = Book(title='Непобедимый', author='Станислав Лем', num_pages=210, isbn=167237, booked=False)
book_2 = Book(title='Клуб оптимистов', author='Жан-Мишель Генассия', num_pages=640, isbn=6607198, booked=False)
book_3 = Book(title='Оплот', author='Теодор Драйзер', num_pages=400, isbn=67929728, booked=False)
book_4 = Book(title='Убивать осознанно', author='Карстен Дюсс', num_pages=290, isbn=65906329, booked=False)
book_5 = Book(title='Медвежий угол', author='Фредрик Бакман', num_pages=420, isbn=40230917, booked=False)

book_3.booked = True

print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)


class SchoolBook(Book):
    tasks = True

    def __init__(self, title, author, num_pages, isbn, subject, grade, booked):
        super().__init__(title, author, num_pages, isbn, booked)
        self.subject = subject
        self.grade = grade

    def __str__(self):
        if self.booked:
            return (f'Название: {self.title}; Автор: {self.author}; страниц: {self.num_pages}; '
                    f'предмет: {self.subject}; класс: {self.grade}; зарезервирована')
        return (f'Название: {self.title}; Автор: {self.author}; страниц: {self.num_pages}; предмет: {self.subject};'
                f' класс: {self.grade}')


book_6 = SchoolBook(title='Логика', author='Чулпанов', num_pages=231, isbn=12447827, subject='Математика',
                    grade=9, booked=False)
book_7 = SchoolBook(title='Биология', author='Лисов', num_pages=331, isbn=67059000, subject='Биология',
                    grade=6, booked=False)
book_8 = SchoolBook(title='Химия', author='Шиманович', num_pages=176, isbn=97898500, subject='Химия',
                    grade=7, booked=False)

book_8.booked = True

print(book_6)
print(book_7)
print(book_8)
