from flask import Blueprint, redirect, url_for, render_template, flash, session
from app.forms import Task_form, Task_update
from app.models import Task, User
from app import db


todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/todo", methods=["GET", "POST"])
def task():
    form = Task_form()

    if form.validate_on_submit():
        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        import datetime

        task = []
        x = datetime.datetime.now()
        task = Task(
            task=form.task.data, date_time=x.strftime("%c"), user_id=session["user_id"]
        )
        db.session.add(task)
        db.session.commit()

        flash("Your Task Added.", "success")
        return redirect(url_for('todo.task_show'))
    return render_template("task_add.html", form=form)

@todo_bp.route("/taskshow", methods=["POST", "GET"])
def task_show():
    if "user_id" in session:
        user_task = Task.query.filter_by(user_id=session["user_id"]).all()
    print(user_task)

    return render_template(
        "task_show.html",
        user_task = user_task
    )

@todo_bp.route('/task_del/<int:task_id>')
def task_del(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo.task_show'))

@todo_bp.route('/task_upd/<int:task_id>', methods = ['GET', 'POST'])
def task_upd(task_id):
    form = Task_update()
    pre_task = Task.query.get(task_id)
    if form.validate_on_submit():
        pre_task.task = form.update_task.data
        pre_task.work = 'Pending'
        db.session.commit()
        flash('Task Update successfully....')
        return redirect(url_for('todo.task_show'))
    return render_template('task_update.html', form = form, pre_task = pre_task)

@todo_bp.route('/toggle/<int:task_id>', methods = ['POST','GET'])
def toggle(task_id):
    task_status = Task.query.get(task_id)
    if task_status.work == 'Pending':
        task_status.work = 'Going On'
        db.session.commit()
    elif task_status.work == 'Going On':
        task_status.work = 'Complete'
        db.session.commit()
    else:
        task_status = 'Complete'
        db.session.commit()
        flash('Task was completed Add new one.')
    return redirect(url_for('todo.task_show'))