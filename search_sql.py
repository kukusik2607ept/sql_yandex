import sqlite3


def searching(search=input("Поиск: ")):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, description
        FROM database_movies
        WHERE title LIKE ? OR title LIKE ? OR description LIKE ? OR description LIKE ?;
    """, (f'%{search.lower()}%', f'%{search.capitalize()}%', f'%{search.lower()}%', f'%{search.capitalize()}%'))
    results = cursor.fetchall()
    conn.close()
    output = ''
    for movie in results:
        output += movie[0] + '\n'
    return output


print(searching())
