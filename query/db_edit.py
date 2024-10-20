import sqlite3

def db_delete(field:str, cond:str):
    """Функция удаляет из БД записи, где одно из заданных полей
    соответствует заданному условию"""
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
         try:
            cur = con.cursor()
            cur.execute(f"DELETE FROM attestation WHERE {field} {cond}")
            if cur.rowcount == 0:
                print("Строки не найдены")
            else:
                confirm = input("Подтвердить изменения? [y/n]: ")
                if confirm == "y":
                    con.commit()
                    print(f"Удалено строк: {cur.rowcount}")
                elif confirm == "n":
                    con.rollback()
                    return
                else:
                    print("Не понимаю. Повторите. ")

         except Exception as err:
             print(f"Произошла ошибка: {err}")


def db_update_field(field:str, cond:str, new):
    """Функция изменяет в таблице ячейку, в определенном поле, которое соответствует
    заданному условию"""
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
        try:
            cur = con.cursor()
            cur.execute((f"UPDATE attestation SET {field} = ? WHERE {field} {cond}"), (new,))
            if cur.rowcount == 0:
                print("Строки не найдены")
            else:
                confirm = input("Подтвердить изменения? [y/n]: ")
                if confirm == "y":
                    con.commit()
                    print(f"Значения поля {field}, соответствующие условию {cond}, изменены на {new}")
                elif confirm == "n":
                    con.rollback()
                    return
                else:
                    print("Не понимаю. Повторите операцию.")

        except Exception as err:
            print(f"Произошла ошибка: {err}")

def db_add(values):
    """Функция добавляет запись в таблицу"""
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
        try:
            cur = con.cursor()
            query = '''INSERT INTO attestation 
                   (sub_code, sub_name, semester, att_type, att_date, 
                   prof_name, prof_status, mark, edit_date)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cur.execute(query, values)

            confirm = input("Подтвердить изменения? [y/n]: ")
            if confirm == "y":
                con.commit()
                print("В таблицу добавлена строка")
                return
            elif confirm == "n":
                con.rollback()
                return
            else:
                print("Не понимаю. Повторите.")
        except Exception as err:
            print(f"Произошла ошибка: {err}")








