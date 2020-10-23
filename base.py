# Студент разрабатывает онлайн-кинотеатр
# У него есть база данных с полями названия и описания фильма.
# Также будут поля с ссылками на видеофайлы
# Необходимо провести поиск по полям названия и описания


import sqlite3
import random

conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()
alpharus = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
alphaeng = list('abcdefghijklmnopqrstuvwxyz')

for i in range(5000):
    rand_num = random.randint(0, 9)
    nameeng = ''
    namerus = ''
    descrip_eng = ''
    descrip_rus = ''
    for j in range(15):
        nameeng += random.choice(alphaeng)
        namerus += random.choice(alpharus)
    for k in range(40):
        descrip_eng += random.choice(alphaeng)
        descrip_rus += random.choice(alpharus)
    print(i)
    if rand_num == 0:
        movie = f'Transformers {i + 1}: {nameeng}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_eng, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 1:
        movie = f'Три богатыря и {namerus.capitalize()}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_rus, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 2:
        movie = f'Pirates of Carribean {i + 1}: {nameeng}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_eng, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 3:
        movie = f'Особенности национальной {namerus}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_rus, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 4:
        movie = f'Star Wars {i + 1}: {nameeng.capitalize()}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_eng, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 5:
        movie = f'Елки {i + 1}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_rus, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 6:
        movie = f'Agent 007. {nameeng.capitalize()}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_eng, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 7:
        movie = f'{namerus.capitalize()}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_rus, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 8:
        movie = f'Terminator {i + 1}. {nameeng.capitalize()}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_eng, random.randint(1, 5000), random.randint(1, 5000)))
    elif rand_num == 9:
        movie = f'Полицейская академия {i + 1}. {namerus.capitalize()}'
        cursor.execute("insert into database_movies values (Null, ?, ?, ?,?);",
                       (movie, descrip_rus, random.randint(1, 5000), random.randint(1, 5000)))
    conn.commit()

conn.close()
