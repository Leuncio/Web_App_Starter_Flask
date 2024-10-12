# __init__.py

from flask import Flask
from flask_bootstrap import Bootstrap5
from .views import main_bp  
from .models import db  

def create_app():
    app = Flask(__name__)  

    # Load configuration from config.py or environment variables
    app.config.from_object('config')

    # Initialize the SQLAlchemy instance with the Flask app
    db.init_app(app)

    # Initialize Bootstrap for styling components
    bootstrap = Bootstrap5(app)

    # Register blueprints for modular routing
    app.register_blueprint(main_bp)

    return app
