import sqlite3

def show_names(cur):
    with sqlite3.connect("vuz3.sqlite") as con:
        cur.execute("PRAGMA table_info(attestation)")
        output = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM attestation")
        count = cur.fetchall()

        headers = [f"{n[1]} ({n[2]})" for n in output]
        format_headers = " | ".join(headers)

        print("Имена и типы полей таблицы attestation: \n", format_headers)
        print("-" * len(format_headers))

        print(f"Количество записей в таблице: {count}")

def table_show(cur):
    with sqlite3.connect("vuz3.sqlite") as con:
        cur.execute("PRAGMA table_info(attestation)")
        fields = cur.fetchall()
        names = [now[1] for now in fields]
        cur.execute("SELECT * FROM attestation")
        rows = cur.fetchall()

        if rows:
            widths = [max(len((name)), max(len(str(row[now])) for row in rows)) for now, name in
                          enumerate(names)]

            header = " | ".join([f"{name:<{widths[now]}}" for now, name in enumerate(names)])
            seps = "-+-".join(['-' * now for now in widths])

            print(header)
            print(seps)

            for now in rows:
                print(" | ".join([f"{str(value):<{widths[i]}}"
                                  for i, value in enumerate(now)]))
        else: print("Таблица пуста!")

def db_saving(file):
    with sqlite3.connect("vuz3.sqlite") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM attestation")
        with open(file, 'w') as f:
            [f.write(str(now) + '\n') for now in cur.fetchall()]
            print(f"Таблица сохранена в файле {file}")

def db_filter(field, condition):
    with sqlite3.connect("vuz3.sqlite") as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM attestation WHERE {field} {condition}")
        rows = cur.fetchall()
        if rows:
            print ("Строки, удовлетворяющие условию:")
            [print(now) for now in rows]
        else: print("Строки не найдены")

def db_delete(field, condition):
    with sqlite3.connect("vuz3.sqlite") as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM attestation WHERE {field} {condition}")
        if cur.rowcount == 0:
            print("Строки не найдены")
        else:
            print(f"Удалено строк: {cur.rowcount}")
        con.commit()

def db_edit(field, condition, new):
    with sqlite3.connect("vuz3.sqlite") as con:
        cur = con.cursor()
        cur.execute((f"UPDATE attestation SET {field} = ? WHERE {condition}"), (new,))
        print(f"Значения поля {field}, соответствующие условию {condition}, изменены на {new}")
        confirm = input("Подтвердить изменения? [y/n]: ")
        if confirm == "y":
            con.commit()
        elif confirm == "n":
            con.rollback()
        else:
            print("Не понимаю. Повторите [y/n]: ")






