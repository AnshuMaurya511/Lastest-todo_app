from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.forms import Resgistration_form
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

register_bp = Blueprint("registers", __name__)


@register_bp.route("/registers", methods=["GET", "POST"])
def sign_up():
    form = Resgistration_form()
    if form.validate_on_submit():

        avaliable_email = User.query.filter_by(email = form.email.data).first()
        if avaliable_email:
            flash("Account Already exist", "danger")
            return redirect(url_for("registers.sign_up"))
    
        encrypt_password = generate_password_hash(form.password.data)
        user = User(
            fullname=form.fullname.data,
            email=form.email.data,
            password=encrypt_password,
        )
        db.session.add(user)
        db.session.commit()

        flash("Account created Successfully.", "success")

        return redirect(url_for("auth.login"))
    return render_template("registers.html", form=form)
