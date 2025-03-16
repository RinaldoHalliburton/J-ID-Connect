from app import app
from flask import render_template, request, redirect, url_for, flash,session,flash
from app.form import  LoginForm,UpdateInfoForm
import mysql.connector
from datetime import datetime




@app.route('/update', methods=['GET','POST'])
def updatedata():
    form = UpdateInfoForm()
    if form.validate_on_submit():
        flash("Documentsubmitted successfully!", 'success')
        return redirect(url_for('userdash'))

    
    
    return render_template('updatedata.html', form=form)

@app.route('/userdash')
def userdash():
    return render_template('userdashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # Initialize connection and cursor to None
    conn = None
    cursor = None

    if request.method == 'POST' and form.validate_on_submit():
        # Grab form data
        username = form.username.data
        password = form.password.data

        try:
            conn = mysql.connector.connect(
                host=app.config['MYSQL_HOST'],
                user=app.config['MYSQL_USER'],
                password=app.config['MYSQL_PASSWORD'],
                database=app.config['MYSQL_DB']
            )
            cursor = conn.cursor(dictionary=True)

            # Query user table for given username
            query = "SELECT * FROM user_profiles WHERE username = %s"
            print(query)
            cursor.execute(query, (username,))
            user = cursor.fetchone()

            if user:
                if user['password'] == password and user['TRN']:
                    session['logged_in'] = True
                    session['title'] = user['Title']
                    session['first_name'] =user['first_name']
                    session['last_name'] = user['last_name']
                    session['email'] = user['Email']
                    session['TRN'] = user['TRN']
                    session['maiden_name'] = user['MaidenName']
                    session['address'] = user['Address']
                    session['telephone'] = user['Telephone']
                    session['maritalstatus'] = user['MaritalStatus']
                    session['occupation'] = user['Occupation']
                    session['gender'] = user['Gender']
                    session['NIS'] = user['NIS']
                    session['username'] = user['username']
                    session['password'] = user['password']
                    session['updated_profile'] = False
                    now = datetime.now()
                    session['current_time'] = now.strftime("%B %d, %Y, %I:%M %p")
                    flash('Logged in successfully!', 'success')
                    return redirect(url_for('userdash'))
                else:
                    flash('Invalid credentials. Please try again.', 'danger')
            else:
                flash('User not found. Please try again.', 'danger')

        except mysql.connector.Error as err:
            flash(f"Database error: {err}", 'danger')
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    return render_template('login.html', form=form)