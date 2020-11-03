from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.main.forms import EditProfileForm
from app.models import User
from datetime import datetime

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/')
@bp.route('/home')
@login_required
def home():
    return render_template('home.html', title = 'Home', username = current_user.username, rooms = ROOMS)

@bp.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first_or_404()
    return render_template('profile.html', title = 'Profile', user = user)

@bp.route('/edit-profile', methods = ['GET', 'POST'])
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved!')
        return redirect(url_for('main.profile', username = current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title = 'Edit Profile', form = form)