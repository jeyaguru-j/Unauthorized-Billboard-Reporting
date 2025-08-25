from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .models import db, UserReport
from .ai_module import detect_billboard
import os

main = Blueprint('main', __name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    message = ''
    result = None
    if request.method == 'POST':
        user_name = request.form['user_name']
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        image = request.files['image']

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)

        result = detect_billboard(image_path)

        report = UserReport(
            user_name=user_name,
            image_path=image_path,
            latitude=latitude,
            longitude=longitude,
            violation_type=result['violation_type'],
            flagged=result['detected']
        )
        db.session.add(report)
        db.session.commit()

        message = f"Report submitted! Flagged: {result['detected']}, Violation Type: {result['violation_type']}"

    return render_template('upload.html', message=message)

@main.route('/dashboard')
def dashboard():
    reports = UserReport.query.all()

    report_list = []
    for r in reports:
        report_list.append({
            "user_name": r.user_name,
            "latitude": r.latitude,
            "longitude": r.longitude,
            "flagged": r.flagged,
            "violation_type": r.violation_type,
            "image_path": r.image_path
        })

    return render_template('dashboard.html', reports=report_list)
