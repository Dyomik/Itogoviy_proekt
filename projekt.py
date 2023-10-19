import sqlite3

def create_db():
    connection = sqlite3.connect('employees.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       full_name TEXT NOT NULL,
                       phone_number TEXT NOT NULL,
                       email_address TEXT NOT NULL,
                       salary REAL NOT NULL)''')
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_db()

import sqlite3

def add_employee(full_name, phone_number, email_address, salary):
    connection = sqlite3.connect('employees.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (full_name, phone_number, email_address, salary) VALUES (?, ?, ?, ?)",
                   (full_name, phone_number, email_address, salary))
    connection.commit()
    connection.close()

def update_employee(employee_id, full_name, phone_number, email_address, salary):
    connection = sqlite3.connect('employees.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE employees SET full_name=?, phone_number=?, email_address=?, salary=? WHERE id=?",
                   (full_name, phone_number, email_address, salary, employee_id))
    connection.commit()
    connection.close()

def delete_employee(employee_id):
    connection = sqlite3.connect('employees.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    connection.commit()
    connection.close()

def search_employee(full_name):
    connection = sqlite3.connect('employees.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees WHERE full_name LIKE ?", ('%'+full_name+'%',))
    results = cursor.fetchall()
    connection.close()
    return results

def main():
    while True:
        print('1. Добавить сотрудника')
        print('2. Изменить сотрудника')
        print('3. Удалить сотрудника')
        print('4. Поиск по ФИО')
        print('0. Выход')
        choice = input('Выберите действие: ')

        if choice == '1':
            full_name = input('Введите ФИО: ')
            phone_number = input('Введите номер телефона: ')
            email_address = input('Введите адрес электронной почты: ')
            salary = float(input('Введите заработную плату: '))
            add_employee(full_name, phone_number, email_address, salary)

        elif choice == '2':
            employee_id = int(input('Введите ID сотрудника: '))
            full_name = input('Введите новое ФИО: ')
            phone_number = input('Введите новый номер телефона: ')
            email_address = input('Введите новый адрес электронной почты: ')
            salary = float(input('Введите новую заработную плату: '))
            update_employee(employee_id, full_name, phone_number, email_address, salary)

        elif choice == '3':
            employee_id = int(input('Введите ID сотрудника: '))
            delete_employee(employee_id)

        elif choice == '4':
            full_name = input('Введите ФИО для поиска: ')
            results = search_employee(full_name)
            if len(results) == 0:
                print('Сотрудников не найдено')
            else:
                for result in results:
                    print(f"ФИО: {result[1]}, Номер телефона: {result[2]}, Адрес электронной почты: {result[3]}, Заработная плата: {result[4]}")

        elif choice == '0':
            break

if __name__ == '__main__':
    main()
