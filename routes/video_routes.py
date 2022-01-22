
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
    VIDEO ROUTES
"""

# @ROUTE: File Route.
# @DESCRIPTION: Renders the video file from the database and onto the client.
@app.route('/file/<id>', methods=["POST", "GET"])
def file(id):
    
    if request.method == "POST":

        pass

    if request.method == "GET":

        clip_id = id
        get_clip = videos_model.VideosModel.query.filter_by(clip_id = clip_id).first();

        return Response(
            get_clip.file,
            mimetype = get_clip.file_mimetype
        )


# @ROUTE: Clip Route.
# @DESCRIPTION: Renders the clip template along with the video content.
@app.route('/clip/<id>', methods=["POST", "GET"])
def clip(id):

    if request.method == "POST":

        pass

    if request.method == "GET":

        clip_id = id

        get_clip = videos_model.VideosModel.query.filter_by(clip_id=clip_id).first()

        get_clip.clip_views += 1
        db.session.commit();

        clip_title = get_clip.clip_title
        clip_views = get_clip.clip_views

        return render_template(
            "clip.html",
            find_clip = clip_id,
            clip_title = clip_title,
            clip_views = clip_views
        )