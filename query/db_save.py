import sqlite3
def db_saving(file):
    """Функция сохраняет все строки в файл без форматирования"""
    with sqlite3.connect("D:/STUDY/NIR/vuz3.sqlite") as con:
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM attestation")
            with open(file, 'w') as f:
                [f.write(str(now) + '\n') for now in cur.fetchall()]
                print(f"Таблица сохранена в файле {file}")
        except Exception:
            raise