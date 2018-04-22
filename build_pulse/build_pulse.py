import os
import json
import sqlite3
from jsonschema import validate
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database.db'),
    SECRET_KEY='key',
    USERNAME='admin',
    PASSWORD='default'
))

schema = {
    "properties" : {
        "make": { "type": "string" },
        "year": { "type": "number" },
        "color": { "type": "string" },
        "price": { "type": "number" },
        "hasSunroof": { "type": "string" },
        "isFourWheelDrive": { "type": "string" },
        "hasLowMiles": { "type": "string" },
        "hasPowerWindows": { "type": "string" },
        "hasNavigation": { "type": "string" },
        "hasHeatedSeats": { "type": "string" },
        "operation": { "type": "string" },
    },
    "required": ["operator"]
}

@app.route('/', methods=['GET'])
def get_all_stock():
    db = get_db();
    values = db.execute("select * from cars").fetchall()
    return json.dumps( [dict(i) for i in values] )

@app.route('/', methods=['POST'])
def get_stock():
    db = get_db();
    entries = request.json

    validate(entries, schema)

    criteria = '';
    operator = entries.pop('operator')

    for key, value in entries.items():
        if len(criteria) > 0:
            criteria += ' ' + operator + ' '

        if value == 'true':
            value = '1'
        elif value == 'false':
            value = '0'

        criteria += key + ' = ' + '"' + value + '"'

    query = "select * from cars where " + criteria + ";"
    values = db.execute("select * from cars where " + criteria).fetchall()
    return json.dumps( [dict(i) for i in values] )

def connect_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
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

@app.cli.command('initdb')
def initdb_command():
    init_db()
    load_db();
    print('Initialized and Loaded the Database.')
