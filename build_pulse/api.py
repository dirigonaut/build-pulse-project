import os
import json
import sqlite3
from jsonschema import validate
from flask import Blueprint, g, request, abort

from db import get_db

bp = Blueprint('api', __name__)

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

@bp.route('/', methods=['GET'])
def get_all_stock():
    db = get_db();
    values = db.execute("select * from cars").fetchall()
    return json.dumps( [dict(i) for i in values] )

@bp.route('/', methods=['POST'])
def get_stock():
    db = get_db();
    entries = request.json

    try:
        validate(entries, schema)
    except:
        abort(400, 'Missing required fields')

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

    try:
        values = db.execute("select * from cars where " + criteria).fetchall()
        return json.dumps( [dict(i) for i in values] )
    except:
        abort(400, 'The data is badly formed')
