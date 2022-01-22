from database_init import db

"""
    VIDEOS DB MODEL
"""

class VideosModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.Text, nullable=False)
    file_name = db.Column(db.Text, nullable=False)
    file_mimetype = db.Column(db.Text, nullable=False)

    clip_title = db.Column(db.Text, nullable=False)
    clip_views = db.Column(db.Integer, nullable=False)
    clip_id = db.Column(db.Integer, nullable=False)