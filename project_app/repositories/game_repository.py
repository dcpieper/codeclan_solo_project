from db.run_sql import run_sql

from models.game import Game
from models.publisher import Publisher
import repositories.publisher_repository as publisher_repository

def save(game):
    sql = "INSERT INTO games (title, developer, publisher_id, genre, wholesale, price, stock) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [game.title, game.developer, game.publisher.id, game.genre, game.wholesale, game.price, game.stock]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)

    for row in results:
        publisher = publisher_repository.select(row['publisher_id'])
        game = Game(row['title'], row['developer'], publisher, row['genre'], row['wholesale'], row['price'], row['stock'], row['id'])
        games.append(game)
    return games

def select(id):
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        publisher = publisher_repository.select(result['publisher_id'])
        game = Game(result['title'], result['developer'], publisher, result['genre'], result['wholesale'], result['price'], result['stock'], result['id'])
        return game

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(game):
    sql = "UPDATE games SET (title, developer, publisher_id, genre, wholesale, price, stock) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [game.title, game.developer, game.publisher.id, game.genre, game.wholesale, game.price, game.stock, game.id]
    run_sql(sql, values)