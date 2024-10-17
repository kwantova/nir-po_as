import sqlite3

def db_delete(field:str, cond:str):
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
                else:
                    print("Не понимаю. Повторите. [y/n]: ")

         except Exception as err:
             raise


def db_update_field(field:str, cond:str, new):
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
        try:
            cur = con.cursor()
            cur.execute((f"UPDATE attestation SET {field} = ? WHERE {cond}"), (new,))
            if cur.rowcount == 0:
                print("Строки не найдены")
            else:
                confirm = input("Подтвердить изменения? [y/n]: ")
                if confirm == "y":
                    con.commit()
                elif confirm == "n":
                    con.rollback()
                else:
                    print("Не понимаю. Повторите. [y/n]: ")

                print(f"Значения поля {field}, соответствующие условию {cond}, изменены на {new}")
        except Exception as err:
            raise

def db_add(values):
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
            elif confirm == "n":
                con.rollback()
            else:
                print("Не понимаю. Повторите. [y/n]: ")

            print("В базу данных добавлена новая запись")
        except Exception as err:
            raise








