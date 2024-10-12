import pytest
from run import create_app
from app.forms import RegisterForm

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_register_form_valid_data(client, app):
    """Test that the RegisterForm is valid with correct data."""
    form_data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'age': 25,
        'password': 'password123',
        'password_confirmation': 'password123'
    }

    with app.test_request_context('/register', method='POST', data=form_data):
        form = RegisterForm()
        assert form.validate()