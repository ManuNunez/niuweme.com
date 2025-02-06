from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes import init_app




def create_app():
    app = Flask(__name__)
    init_app(app)


    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('development/under_development.html'), 404
    
    return app
