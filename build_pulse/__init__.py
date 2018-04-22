import os
from flask import Flask, g

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database.db'),
    SECRET_KEY='key',
    USERNAME='admin',
    PASSWORD='default'
))

from build_pulse import db
db.init_app(app)

from build_pulse import api
app.register_blueprint(api.bp)

def get_app():
    return app
