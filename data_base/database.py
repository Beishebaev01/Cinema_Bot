import sqlite3
from parser.parser_from_ts_kg import get_data_from_page, get_html


def sql_create():
    global db, cursor
    db = sqlite3.connect("films.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подлючена!")

    db.execute("CREATE TABLE IF NOT EXISTS films"
               "(title VARCHAR (100),"
               "link TEXT)")
    # cursor.execute("INSERT INTO films (title, link) VALUES ()")
    db.commit()
