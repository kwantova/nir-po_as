import sqlite3

import query.db_edit as e
import query.db_show as sh
import query.db_save as s

def menu():
    print("""--- ВЫБЕРИТЕ ОПЦИЮ ---
    [f] Показать список полей таблицы
    [a] Показать всю таблицу
    [s] Сохранить содержимое таблицы в файл
    [w] Фильтр по полю
    [d] Удалить данные по условию
    [u] Изменить содержимое по условию
    [i] Добавить новую строкy
    [q] Выйти""")
    return input("Выберите действие: ")

while True:
    option = menu()

    if option == "f":
        sh.show_names()

    elif option == "a":
        sh.table_show()

    elif option == "s":
        file = input("Введите имя файла для сохранения: ")
        s.db_saving(file)

    elif option == "w":
        while True:
            try:
                field = input("Введите имя поля, к которому применяется условие: ")
                cond = input("Введите условие фильтрации: ")
                sh.db_filter(field, cond)
                break
            except Exception as err:
                print (f"Возникла ошибка: {err}. Повторите ввод:")

    elif option == "d":
        while True:
            try:
                field = input("Введите имя поля, к которому применяется условие: ")
                cond = input("Введите условие фильтрации: ")
                e.db_delete(field, cond)
                break
            except Exception as err:
                print(f"Возникла ошибка: {err}. Повторите ввод:")

    elif option == "u":
        while True:
            try:
                field = input("Введите имя поля, к которому применяется условие: ")
                cond = input("Введите условие фильтрации: ")
                new = input("Введите через пробел или запятую данные: ").split()
                break
            except Exception as err:
                print(f"Возникла ошибка: {err}. Повторите ввод:")


    elif option == "i":
        while True:
            try:
                field = input("Введите имя поля, к которому применяется условие: ")
                cond = input("Введите условие фильтрации: ")
                vals = input("Введите через пробел или запятую данные").split()
                e.db_add(vals)
                break
            except Exception as err:
                print(f"Возникла ошибка: {err}. Повторите ввод:")

    elif option == "q":
        print("Сеанс работы завершен")
        break





