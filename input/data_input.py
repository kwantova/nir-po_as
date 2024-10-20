from datetime import datetime
import query.db_edit as e
def hints_input():
    vals = [0] * 9
    vals[0] = input("Код дисциплины по учебному плану [текст]: ")
    vals[1] = input("Название дисциплины [текст]: ")
    vals[2] = int(input("Номер семестра с аттестацией по дисциплине [целое число]: "))
    vals[3] = input("Тип аттестации (экзамен/зачет) [текст]: ").lower()
    vals[4] = input("Дата аттестации в формате DD.MM.YYYY [текст]: ")
    vals[5] = input("ФИО преподавателя, проводившего аттестацию [текст]: ")
    select_status = ["ассистент", "преподаватель", "старший преподаватель", "доцент", "профессор",
                     "заведующий кафедрой"]
    status_str = "\n".join([f"* {i}" for i in select_status])
    vals[6] = input(f"Выберите должность: \n{status_str}\nДолжность преподавателя [строка]: ")
    vals[7] = int(input("Полученная оценка [целое число]: "))
    vals[8] = datetime.today().strftime('%d.%m.%Y')
    if (vals[6] in select_status) and (vals[7] in [2,3,4,5]) and (vals[3] in ["экзамен", "зачет", "зачёт"]):
        return vals
    else:
        print("Данные не соответствуют диапазонам. Повторите выполнение операции.")
        return -1

def file_input(file, lines_to_read):
    with open(file, 'r', encoding='utf-8') as f:
        try:
            if lines_to_read == sum(1 for _ in f):
                f.seek(0) #Возврат указателя обратно в начало
                lines = f.readlines()
            else:
                # Преобразуем количество строк в число и читаем соответствующее количество строк
                lines = [next(f) for _ in range(int(lines_to_read))]

            for line in lines:
                # Разбиваем строку на элементы по пробелам и очищаем от лишних символов (например, \n)
                data = line.strip().split()
                for i in range(len(data)):
                    if "_" in data[i]:
                        data[i] = data[i].replace("_", " ")

                if len(data) == 8:  # Убедимся, что в строке ровно 8 элементов
                    data.append(datetime.today().strftime('%d.%m.%Y'))
                    e.db_add(data)
                else:
                    print(f"Ошибка: строка не содержит 8 элементов. Пропускаем строку: {line.strip()}")
        except Exception as err: print(f"Произошла ошибка: {err}")

def confirm_changes(con):
    confirm = input("Подтвердить изменения? [y/n]: ")
    if confirm == "y":
        con.commit()
        print("В таблицу добавлена строка")
        return
    elif confirm == "n":
        con.rollback()
        return
    else:
        print("Не понимаю. Повторите. [y/n]: ")