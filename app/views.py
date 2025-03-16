import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.models import UserProfile
from app.form import UpdateInfoForm, LoginForm
from models import db, Patient
#from .forms import UploadForm

@app.route('/search', methods=['GET'])
def search_patients():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    results = Patient.query.filter(
        (Patient.first_name.ilike(f"%{query}%")) |
        (Patient.last_name.ilike(f"%{query}%")) |
        (Patient.medical_record_number.ilike(f"%{query}%")) |
        (Patient.diagnosis.ilike(f"%{query}%"))
    ).all()

    response = [
        {
            "id": patient.id,
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "dob": patient.dob,
            "medical_record_number": patient.medical_record_number,
            "diagnosis": patient.diagnosis,
            "last_visit": patient.last_visit
        }
        for patient in results
    ]

    return jsonify(response)


@app.route('/update', methods=['GET','POST'])
def updatedata():
    form = UpdateInfoForm()
    if form.validate_on_submit():
        flash("Documentsubmitted successfully!", 'success')
        #return redirect(url_for('index'))
    
    return render_template('updatedata.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You are logged out")
    return redirect(url_for('home'))

@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    form = UploadForm()

    if request.method=='GET':
        render_template('upload.html', form=form)
    elif request.method=='POST':
        if form.validate_on_submit():
            image_file = form.image.data
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)

            flash('File Saved', 'success')
            return redirect(url_for('home')) 

    return render_template('upload.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Grab form data
        username = form.username.data
        password = form.password.data
        
        # Example: Replace with your user-auth logic
        # e.g., check a real database, verify a hashed password, etc.
        if username == 'admin' and password == 'secret123':
            # Mark user as logged in
            session['logged_in'] = True
            flash('Logged in successfully!', 'success')
            return redirect(url_for('views.dashboard'))  # Example: some protected route
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html', form=form)