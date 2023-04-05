import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("films.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подлючена!")

    db.execute("CREATE TABLE IF NOT EXISTS films"
               "(title VARCHAR (100),"
               "link TEXT)")
    db.commit()
    db.close()


def sql_command_insert(film):
    with sqlite3.connect("films.sqlite3", isolation_level=None) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO films VALUES (?, ?)", tuple(film.values()))