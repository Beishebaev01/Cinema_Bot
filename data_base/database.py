import sqlite3
import random

db = sqlite3.connect("films.sqlite")
cursor = db.cursor()


def sql_create():
    if db:
        print("База данных подлючена!")

    db.execute("CREATE TABLE IF NOT EXISTS films"
               "(id INTEGER PRIMARY KEY ,"
               "title VARCHAR (100),"
               "link TEXT)")
    db.commit()


async def sql_command_insert(film):
    with sqlite3.connect("films.sqlite", isolation_level=None) as db:
        cursor.execute("INSERT INTO films VALUES (?, ?, ?) ", tuple(film.values()))


async def sql_command_random():
    result = cursor.execute("SELECT * FROM films").fetchall()
    random_film = random.choice(result)
    randomfilm = (random_film[1], random_film[2])
    return randomfilm


async def sql_command_all():
    return cursor.execute("SELECT * FROM films").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM films WHERE id = ?", (id,))
    db.commit()


async def sql_command_clear():
    cursor.execute("DELETE FROM films WHERE id>=1")

# def sql_command_find_film(response):
#     cursor.execute("SELECT * FROM films WHERE title LIKE ")
