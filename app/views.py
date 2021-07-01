from flask import render_template, flash, redirect, url_for
from app import app
from app import db
# from app.forms import LoginForm, RegistrationForm
from app.models import User2
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse


# def not_logged_in():
#     return render_to_template('index.html')

def view_fn():
    if not current_user:
        # Anonymous user
        return redirect(url_for('not_logged_in'))
    elif 'admin' in current_user.type:
        # admin page
        return redirect(url_for('admindashboard'))
    elif 'student' in current_user.type:
        # student page
        return redirect(url_for('studentdashboard'))
    elif 'tutor' in current_user.type:
        # tutor page
        return redirect(url_for('tutordashboard'))
