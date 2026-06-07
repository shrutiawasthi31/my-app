from flask import Flask, render_template, request, redirect, session, url_for
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Dummy user database
USERS = {
    'admin': 'password123',
    'user': 'user123'
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', user=session.get('user'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and USERS[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials'), 401
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard page - requires login"""
    user = session.get('user')
    dashboard_data = {
        'user': user,
        'stats': {
            'projects': 12,
            'tasks_completed': 45,
            'team_members': 8
        }
    }
    return render_template('dashboard.html', data=dashboard_data)

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
