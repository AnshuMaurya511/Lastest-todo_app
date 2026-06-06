from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    import os
    from dotenv import load_dotenv

    load_dotenv()

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", 'default-fallback-key')

    app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
    )


    app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
    app.config['MYSQL_USER'] = os.getenv('DB_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('DB_NAME')

    db.__init__(app)



    from app.routes.registers import register_bp
    app.register_blueprint(register_bp, url_prefix="/register")

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.routes.todo import todo_bp
    app.register_blueprint(todo_bp, url_prefix ='/todo')

    @app.route("/")
    def start_app():
        from flask import redirect, url_for

        return redirect(url_for("registers.sign_up"))

    return app


from app import create_app
