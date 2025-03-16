from app import app
from flask import render_template, request, redirect, url_for, flash,session
from app.form import UpdateInfoForm, LoginForm




@app.route('/update', methods=['GET','POST'])
def updatedata():
    form = UpdateInfoForm()
    if form.validate_on_submit():
        flash("Documentsubmitted successfully!", 'success')
        #return redirect(url_for('index'))
    
    return render_template('updatedata.html', form=form)

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

