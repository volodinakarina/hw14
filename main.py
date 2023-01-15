from flask import Flask, jsonify
from utils import *

app = Flask(__name__)


@app.route("/movie/<title>")
def movie_by_name(title):
    movie = get_movie_by_name(title)
    return jsonify(movie)


@app.route("/movie/<int:year_start>/to/<int:year_end>")
def movie_by_years(year_start, year_end):
    movies = get_movie_by_years(year_start, year_end)
    return jsonify(movies)


@app.route("/rating/children")
def movie_for_children():
    movies = get_movies_for_children()
    return jsonify(movies)


@app.route("/rating/family")
def movie_for_family():
    movies = get_movies_for_family()
    return jsonify(movies)


@app.route("/rating/adults")
def movie_for_adults():
    movies = get_movies_for_adults()
    return jsonify(movies)


@app.route("/genre/<genre>")
def movie_by_genre(genre):
    movies = get_movie_by_genre(genre)
    return jsonify(movies)


if __name__ == '__main__':
    app.run(debug=True)
