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


def sql_command_insert(film: dict):
    cursor.execute("INSERT INTO films(title, link) VALUES (title, link)",
                    (film.get('title'), film.get('link')))
    db.commit()
