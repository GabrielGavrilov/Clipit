
#   Clipit - A simple video sharing platform.
#   @version 1.0.0
#   @authors Gabriel Gavrilov <gabrielgavrilov11@gmail.com>

"""
    NECESSARY SERVER IMPORTS
"""

from random import randrange
import json
from random import random
from flask import Flask, redirect, url_for, render_template, request, Response
from werkzeug.utils import secure_filename
from database_init import db, db_init
from models import videos_model

"""
    SERVER SETUP
"""

with open('./private_constants.json') as jf:
    private_constants = json.load(jf)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = private_constants["SQLALCHEMY_DB_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.static_folder = './static'
db_init(app)

@app.before_first_request
def create_tables():
    db.create_all()

"""
    IMPORT WEB ROUTES
"""

from routes import home_routes
from routes import upload_routes
from routes import video_routes

"""
    RUN THE FLASK APPLICATION
"""

if __name__ == "__main__":
    app.run(debug=True)