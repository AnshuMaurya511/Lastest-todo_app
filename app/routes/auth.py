from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.models import User,Task
from app import db
from app.forms import Login_form
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/auth", methods = ['GET', 'POST'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        
        avaliable_user = User.query.filter_by(email = form.email.data).first()
        if avaliable_user and  check_password_hash(avaliable_user.password, form.password.data): 
            session['user_id'] = avaliable_user.id
            flash('You Are Login.', 'success')
            return redirect(url_for('todo.task'))
        else:
            flash('Account are not exist.', 'danger')
            return redirect(url_for('registers.sign_up'))
    
    return render_template("auth.html", form=form)

@auth_bp.route('/log_out')
def log_out():
        session.pop('user_id', None)
        flash('Successfully Logout', 'success')
        return redirect(url_for('registers.sign_up'))


