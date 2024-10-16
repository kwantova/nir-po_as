import sqlite3

def show_names(cur):
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
        

