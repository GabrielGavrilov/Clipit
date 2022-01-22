
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
    UPLOAD ROUTES
"""

# @ROUTE: Upload Route.
# @DESCRIPTION: Uploads the selected video onto the database.
@app.route('/upload', methods=["POST", "GET"])
def upload():

    if request.method == "POST":

        file = request.files["clip_upload"]
        filename = secure_filename(file.filename)
        mimetype = file.mimetype
        clip_title = request.form["clip_title"]
        clip_views = 0
        clip_id = randrange(10000000, 99999999)

        if clip_title == "":
            clip_title = "untitled - " + str(clip_id)

        elif clip_title:
            pass

        if len(clip_title) >=41:
            clip_title = "untitled - " + str(clip_id)
            
        else:
            pass

        if mimetype != "video/mp4":
            return redirect(
                url_for("home")
            )

        new_clip = videos_model.VideosModel(
            file = file.read(),
            file_name = filename,
            file_mimetype = mimetype,
            clip_title = clip_title,
            clip_views = clip_views,
            clip_id = clip_id
        )

        db.session.add(new_clip)
        db.session.commit()

        return redirect(
            url_for("clip", id = clip_id)
        )

    if request.method == "GET":

        return redirect(
            url_for("home")
        )