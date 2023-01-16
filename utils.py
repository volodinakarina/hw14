import sqlite3


def get_all(query: str):
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row

        result = []

        for item in conn.execute(query).fetchall():
            result.append(dict(item))

        return result


def get_movie_by_name(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE '%{title}%'
                ORDER BY release_year DESC"""
        )

        data = cursor.fetchone()

        film = {"title": data[0],
                "country": data[1],
                "release_year": data[2],
                "genre": data[3],
                "description": data[4]}

        return film


def get_movie_by_years(year_start, year_end):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {year_start} AND {year_end}
            LIMIT 100         
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "release_year": i[1]}
            film_list.append(film)
        return film_list


def get_movies_for_children():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, rating, description
           FROM netflix
           WHERE rating='G'
           LIMIT 100
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "rating": i[1], "description": i[2]}
            film_list.append(film)
        return film_list


def get_movies_for_family():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, rating, description
           FROM netflix
           WHERE rating='G' OR rating='PG' OR rating='PG-13'
           LIMIT 100
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "rating": i[1], "description": i[2]}
            film_list.append(film)
        return film_list


def get_movies_for_adults():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, rating, description
           FROM netflix
           WHERE rating='R' OR rating='NC-17'
           LIMIT 100
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "rating": i[1], "description": i[2]}
            film_list.append(film)
        return film_list


def get_movie_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC 
            LIMIT 10
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "description": i[1]}
            film_list.append(film)

        return film_list


def search_by_cast(name1: str = 'Rose McIver', name2: str = 'Ben Lamb'):
    query = f"""
        SELECT * FROM netflix
        WHERE "cast" LIKE '%Rose McIver%'
        AND "cast" LIKE '%Ben Lamb%'
        """

    cast = []
    set_cast = set()
    result = get_all(query)

    for item in result:
        for actor in item['cast'].split(','):
            cast.append(actor)

    for actor in cast:
        if cast.count(actor) > 2:
            set_cast.add(actor)

    return list(set_cast)


def find_movie(type, release_year, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, description
            FROM netflix
            WHERE type LIKE '%{type}%' AND release_year = {release_year} AND listed_in LIKE '%{genre}%'
            LIMIT 10
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "description": i[1]}
            film_list.append(film)

        return film_list
