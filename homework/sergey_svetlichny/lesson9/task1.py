class Book:
    page_material: str
    is_text_present: bool
    name: str
    author: str
    pages_qty: int
    # isbn: str
    reserved: bool

    def __init__(self, page_material, is_text_present, name, author, pages_qty, reserved):
        self.page_material = page_material
        self.is_text_present = is_text_present
        self.name = name
        self.author = author
        self.pages_qty = pages_qty
        self.reserved = reserved
        self.is_reserved()

    def is_reserved(self):
        if self.reserved == True:
            return ', зарезервирована'
        else:
            return ''


book_1 = Book('бумага', True, 'Отверженные', 'Виктор Гюго', 496, False)
book_2 = Book('бумага', True, 'Робинзон Крузо', 'Даниэдь Дефо', 274, False)
book_3 = Book('бумага', False, 'Вокруг света за 80 дней', 'Жюль Верн', 405, False)
Book.isbn = ''
book_3.isbn = '978-5-9287-3204-2'
book_4 = Book('бумага', True, 'Подземелья черного замка', 'Дмитрий Браславский', 342, True)
book_4.isbn = '978-5-905195-11-2'
book_5 = Book('бумага', True, 'На западном фронте без перемен', 'Эрих Мария Ремарк', 396, False)

book_list = (book_1, book_2, book_3, book_4, book_5)
for x in book_list:
    print('Название: ' + x.name, ', Автор: ' + x.author, ', страниц: ' + str(x.pages_qty),
          ', материал: ' + x.page_material, x.is_reserved())


class Schoolbook(Book):
    subject: str
    group: str
    is_task_present: bool

    def __init__(self, page_material, is_text_present, name, author, pages_qty, reserved, subject, group,
                 is_task_present):
        super().__init__(page_material, is_text_present, name, author, pages_qty, reserved)
        super().is_reserved()
        self.subject = subject
        self.group = group
        self.is_task_present = is_task_present


schoolbook_1 = Schoolbook('бумага', True, 'Алгебра', 'Перельман', 195, True, 'Математика', 9, True)
schoolbook_2 = Schoolbook('бумага', False, 'Геометрия', 'Перельман', 206, False, 'Математика', 6, True)
schoolbook_3 = Schoolbook('бумага', True, 'География Евразии', 'Птушкин', 274, True, 'География', 5, False)
schoolbook_4 = Schoolbook('бумага', True, 'Информатика', 'Билл Гейтс', 332, False, 'Информатика', 8, False)
schoolbook_5 = Schoolbook('бумага', True, 'Астрономия', 'Илон Маск', 184, True, 'Астрономия', 11, False)
print()
schoolbook_list = (schoolbook_1, schoolbook_2, schoolbook_3, schoolbook_4, schoolbook_5)
for x in schoolbook_list:
    print('Название: ' + x.name, ', Автор: ' + x.author, ', страниц: ' + str(x.pages_qty),
          ', предмет: ' + x.subject, ', класс: ' + str(x.group), x.is_reserved())
