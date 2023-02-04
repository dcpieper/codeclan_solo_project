from db.run_sql import run_sql

from models.game import Game
from models.publisher import Publisher

def save(publisher):
    sql = "INSERT INTO publishers (name, contact_details) VALUES (%s, %s) RETURNING *"
    values = [publisher.name, publisher.contact_details]
    results = run_sql(sql, values)
    id = results[0]['id']
    publisher.id = id
    return publisher

def select_all():
    publishers = []

    sql = "SELECT * FROM publishers"
    results = run_sql(sql)

    for row in results:
        publisher = Publisher(row['name'], row['contact_details'], row['id'])
        publishers.append(publisher)
    return publishers

def select(id):
    publisher = None
    sql = "SELECT * FROM publishers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        publisher = Publisher(result['name'], result['contact_details'], result['id'])
    return publisher

def delete_all():
    sql = "DELETE FROM publishers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM publishers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(publisher):
    sql = "UPDATE publishers SET (name, contact_details) = (%s, %s) WHERE id = %s"
    values = [publisher.name, publisher.contact_details, publisher.id]
    run_sql(sql, values)

def games(publisher):
    games = []

    sql = "SELECT * FROM games WHERE publisher_id = %s"
    values = [publisher.id]
    results = run_sql(sql, values)

    for row in results:
        game = Game(row['title'], publisher, row['genre'], row['wholesale'], row['price'], row['stock'], row['id'])
        games.append(game)
    return games