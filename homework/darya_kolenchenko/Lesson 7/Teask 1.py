import datetime

while True:
    user_date = input('Enter the date: ')
    try:
        python_date = datetime.datetime.strptime(user_date, '%d-%m-%Y')
        print(python_date, '- Python date')
    except ValueError:
        print('Incorrect date format. Please, use format dd-mm-yyyy (example 25-12-2014)')
