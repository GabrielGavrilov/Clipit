
"""
    NECESSARY SERVER IMPORTS
"""

from random import randrange
import json
from random import random
from app import app, redirect, url_for, render_template, request, Response
from werkzeug.utils import secure_filename
from database_init import db, db_init
from models import videos_model

"""
	HOME ROUTES
"""

# @ROUTE: Home Route.
# @DESCRIPTION: Renders the home template.
@app.route('/', methods=["POST", "GET"])
def home():

    if request.method == "POST":
     
        pass

    if request.method == "GET":

        return render_template(
            "home.html"
        )