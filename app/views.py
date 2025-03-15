import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.models import UserProfile
from app.forms import LoginForm
from werkzeug.security import generate_password_hash
from .forms import UploadForm



@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Get the username and password values from the form.
        res = request.form
        formUsername = res['username']
        formPassword = res['password']

        user = UserProfile.query.filter_by(username = formUsername)
        # Gets user id, load into session
        if check_password_hash(user[0].password, formPassword):
            login_user(user[0])

            flash("Login successful")
            return redirect(url_for("home")) 
    return render_template("login.html", form=form)

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