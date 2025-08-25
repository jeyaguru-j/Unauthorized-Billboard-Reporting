from . import db
from datetime import datetime

class UserReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    image_path = db.Column(db.String(200))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    violation_type = db.Column(db.String(100))
    flagged = db.Column(db.Boolean, default=False)
