import sqlite3

def show_names():
    """Функция возвращает имена полей таблицы"""
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
        cur = con.cursor()
        cur.execute("PRAGMA table_info(attestation)")
        output = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM attestation")
        count = cur.fetchone()[0]   # Используем fetchone и извлекаем число

        headers = [f"{n[1]} ({n[2]})" for n in output]
        format_headers = " | ".join(headers)

        print("Имена и типы полей таблицы attestation: \n", format_headers)
        print("-" * len(format_headers))

        print(f"Количество записей в таблице: {count}")

def table_show():
    """Функция возвращает всё содержимое таблицы, форматировав внешний вид с помощью
    символов ASCII, сверху подписаны поля"""
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
        cur = con.cursor()
        cur.execute("PRAGMA table_info(attestation)")
        fields = cur.fetchall()

        if not fields:
            print("Таблица 'attestation' не существует.")
            return

        names = [now[1] for now in fields]
        cur.execute("SELECT * FROM attestation")
        rows = cur.fetchall()

        if not rows:
            print("Таблица пуста!")
            return
        widths = [max(len((name)), max(len(str(row[now])) for row in rows)) for now, name in
                      enumerate(names)]

        header = " | ".join([f"{name:<{widths[now]}}" for now, name in enumerate(names)])
        seps = "-+-".join(['-' * now for now in widths])

        print(header)
        print(seps)

        for now in rows:
            print(" | ".join([f"{str(value):<{widths[i]}}"
                              for i, value in enumerate(now)]))

def db_filter(field:str, cond:str):
    """Функция возвращает поля, соответствующие условию.
    Если условие введено некорректно и не выполнилось, возвращается ошибка"""
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM attestation WHERE {field} {cond}")
            rows = cur.fetchall()
            if rows:
                print("Строки, удовлетворяющие условию:")
                [print(now) for now in rows]
            else:
                print("Строки не найдены")
        except Exception as err:
            raise

