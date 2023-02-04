from flask import Flask, render_template, request, redirect
from repositories import game_repository
from repositories import publisher_repository
from models.game import Game

from flask import Blueprint

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", all_games = games)

@games_blueprint.route("/games/new", methods=['GET'])
def new_task():
    publishers = publisher_repository.select_all()
    return render_template("games/new.html", all_publishers = publishers)

@games_blueprint.route ("/games", methods=['POST'])
def create_game():
    title = request.form['title']
    developer = request.form['developer']
    publisher_id = request.form['publisher_id']
    genre = request.form['genre']
    wholesale = request.form['wholesale']
    price = request.form['price']
    stock = request.form['stock']
    publisher = publisher_repository.select(publisher_id)
    game = Game(title, developer, publisher, genre, wholesale, price, stock)
    game_repository.save(game)
    return redirect('/games')

@games_blueprint.route("/games/<id>", methods=['GET'])
def show_game(id):
    game = game_repository.select(id)
    return render_template('games/show.html', showGame = game)

@games_blueprint.route("games/<id>", methods=['POST'])
def update_game(id):
    title = request.form['title']
    developer = request.form['developer']
    publisher_id = request.form['publisher_id']
    genre = request.form['genre']
    wholesale = request.form['wholesale']
    price = request.form['price']
    stock = request.form['stock']
    publisher = publisher_repository.select(publisher_id)
    game = Game(title, developer, publisher, genre, wholesale, price, stock, id)
    game_repository.update(game)
    return redirect("/games")

@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_game(id):
    game_repository.delete(id)
    return redirect('/games')