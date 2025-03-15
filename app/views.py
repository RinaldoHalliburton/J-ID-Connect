import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
# app.models import UserProfile
#from app.form import SignupForm
#from app.forms import UploadForm
from flask import send_from_directory
import cv2
import numpy as np
import requests
import base64




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        trn = request.form.get('trn')
        
        #ID card upload
        idcard = request.files.get('idcard')
        if not idcard:
            flash("ID card is required.", "danger")
            return redirect(url_for('signup'))

        id_filename = secure_filename(idcard.filename)
        idpath = os.path.join(app.config['UPLOAD_FOLDER'], id_filename)
        idcard.save(idpath)

        # Handle face scan (Base64 image from JS)
        facescan_data = request.form.get('facescan')
        if not facescan_data:
            flash("Face scan is required.", "danger")
            return redirect(url_for('signup'))

        facescan_data = facescan_data.split(',')[1]  
        facepath = os.path.join(app.config['UPLOAD_FOLDER'], "facescan.png")
        with open(facepath, "wb") as file:
            file.write(base64.b64decode(facescan_data))

        # facial recognition
        if not detect_face(facepath):
            flash("No face detected. Please try again.", "danger")
            return redirect(url_for('signup'))

        # Send data to admin
        admin_url = "http://example.com/admin_verify"  # Replace with actual endpoint
        data = {'name': name, 'trn': trn}

        try:
            with open(idpath, 'rb') as id_file, open(facepath, 'rb') as face_file:
                files = {'idcard': id_file, 'facescan': face_file}
                response = requests.post(admin_url, data=data, files=files)

            if response.status_code == 200:
                flash("Signup submitted successfully!", "success")
            else:
                flash("Error sending data to admin.", "danger")
        except Exception as e:
            flash(f"Failed to connect to admin: {e}", "danger")

        return redirect(url_for('signup'))

    return render_template('signup.html')

def detect_face(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return len(faces) > 0  