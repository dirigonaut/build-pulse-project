import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(initdb_command)

def connect_db():
    db = sqlite3.connect(current_app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def load_db():
    db = get_db()
    cars = json.load(open(os.path.join(os.path.dirname(__file__), "data.json")))

    query = "insert into cars values (?,?,?,?,?,?,?,?,?,?,?)"
    columns = [ "_id", "make", "year", "color", "price",
      "hasSunroof", "isFourWheelDrive", "hasLowMiles",
      "hasPowerWindows", "hasNavigation", "hasHeatedSeats"]

    for entry in cars:
        values = () + tuple(entry[c] for c in columns)
        db.execute(query, values)
        db.commit()

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@click.command('init-db')
@with_appcontext
def initdb_command():
    init_db()
    load_db()
    print('Initialized and Loaded the Database.')
