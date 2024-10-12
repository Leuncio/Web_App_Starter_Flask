# views.py

from flask import Blueprint, request, render_template, url_for, redirect, flash, session
from .forms import RegisterForm

# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterForm()

    return render_template('index.html', form=form)