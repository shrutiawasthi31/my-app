import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Test that login page loads"""
    response = client.get('/login')
    assert response.status_code == 200

def test_invalid_login(client):
    """Test login with invalid credentials"""
    response = client.post('/login', data={
        'username': 'invalid',
        'password': 'wrong'
    })
    assert response.status_code == 401

def test_valid_login(client):
    """Test login with valid credentials"""
    response = client.post('/login', data={
        'username': 'admin',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_dashboard_requires_login(client):
    """Test that dashboard redirects to login when not authenticated"""
    response = client.get('/dashboard')
    assert response.status_code == 302  # Redirect

def test_404_error(client):
    """Test 404 error page"""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
