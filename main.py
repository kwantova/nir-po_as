import query.db_edit as e
import query.db_show as sh
import query.db_save as s
from input import data_input as i


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

    if option.lower() == "f":
        sh.show_names()

    elif option.lower() == "a":
        sh.table_show()

    elif option.lower() == "s":
        try:
            file = input("Введите имя файла для сохранения: ")
            s.db_saving(file)
        except Exception as e:
            print (f"Ошибка: {e}")

    elif option.lower() == "w":
        while True:
            try:
                field = input("Введите имя поля, к которому применяется условие: ")
                cond = input("Введите условие фильтрации: ")
                sh.db_filter(field, cond)
                break
            except Exception as err:
                print (f"Возникла ошибка: {err}. Повторите ввод:")

    elif option.lower() == "d":
        while True:
            try:
                field = input("Введите имя поля, к которому применяется условие: ")
                cond = input("Введите условие фильтрации: ")
                e.db_delete(field, cond)
                break
            except Exception as err:
                print(f"Возникла ошибка: {err}. Повторите ввод:")

    elif option.lower() == "u":
        while True:
            try:
                field = input("Введите имя поля, к которому применяется условие: ")
                cond = input("Введите условие фильтрации: ")
                new = input("Введите новое значение: ")
                e.db_update_field(field, cond, new)
                break
            except Exception as err:
                print(f"Возникла ошибка: {err}. Повторите ввод:")


    elif option.lower() == "i":
        while True:
            try:
                print("[h] - Построчный ввод с подсказками (подписан тип и имя поля)")
                print("[f] - Ввод из файла")
                type = input("Выберите тип ввода: ")

                if type == "h" or type == "H":
                    vals = i.hints_input()
                    if vals != -1:
                        e.db_add(vals)
                    break

                elif type == "f" or type == "F":
                    try:
                        file = input("Введите имя файла: ")
                        custom_lines = input("Хотите указать количество строк? \nПри отказе считаются все строки [y/n]: ")
                        if custom_lines.lower() == "y":
                            lines_to_read = input("Введите количество строк для считывания: ")
                        else:
                            count = sum(1 for _ in open(file, "r", encoding="utf-8"))
                            lines_to_read = count
                        i.file_input(file, lines_to_read)
                        break

                    except Exception as err:
                        print(f"Ошибка: {err}.")

            except Exception as err:
                print(f"Возникла ошибка: {err}. Повторите ввод:")

    elif option.lower() == "q":
        print("Сеанс работы завершен")
        break
    else:
        print ("Команда не распознана. Повторите ввод.")





