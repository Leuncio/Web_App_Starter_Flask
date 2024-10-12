# config.py

import os
from dotenv import load_dotenv

# Automatically load environment variables from .env
load_dotenv()

# Set the URI for the database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'

# Add the secret key for CSRF protection
SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'