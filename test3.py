import os, sqlite3

def select_cmd():
    sql = "SELECT * FROM {}".format(tblname)
    with con:
        data = cur.execute(sql).fetchall()
    return (data)

dbname = ""

while not os.path.isfile(dbname):
    dbname = input("Укажите имя файла SQlite: ")
    if os.path.isfile(dbname): break
    print("Нет такого файла!")

tblname = input("Укажите имя таблицы: ")
con = sqlite3.connect(dbname)
cur = con.cursor()
dan = select_cmd()
nzap = len(dan)

print("Таблица: ", tblname, "из БД ", dbname)
for i in range(nzap):
    print(dan[i])

cur.close()
con.close()
    
