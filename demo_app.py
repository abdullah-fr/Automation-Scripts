"""
Demo Web Application - Login & Signup System
A simple Flask app to practice automation testing properly
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'demo_secret_key_for_testing'

# In-memory user database (for demo purposes)
users_db = {
    'test@example.com': {
        'password': 'Test123!',
        'first_name': 'Test',
        'last_name': 'User'
    }
}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        # Validation
        if not email:
            flash('Email is required', 'error')
            return render_template('login.html')

        if not password:
            flash('Password is required', 'error')
            return render_template('login.html')

        # Check credentials
        if email in users_db and users_db[email]['password'] == password:
            session['user'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
            return render_template('login.html')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Validation
        errors = []

        if not first_name:
            errors.append('First name is required')

        if not last_name:
            errors.append('Last name is required')

        if not email:
            errors.append('Email is required')
        elif '@' not in email or '.' not in email:
            errors.append('Invalid email format')

        if not password:
            errors.append('Password is required')
        elif len(password) < 6:
            errors.append('Password must be at least 6 characters')

        if password != confirm_password:
            errors.append('Passwords do not match')

        if email in users_db:
            errors.append('Email already registered')

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('signup.html')

        # Create user
        users_db[email] = {
            'password': password,
            'first_name': first_name,
            'last_name': last_name
        }

        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('login'))

    user_email = session['user']
    user_data = users_db.get(user_email, {})

    return render_template('dashboard.html', user=user_data)


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    # Create templates directory
    os.makedirs('templates', exist_ok=True)

    print("Demo app running at http://localhost:5000")
    print("Test credentials: test@example.com / Test123!")
    app.run(debug=True, port=5000)
