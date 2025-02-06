from flask import Flask
from app.routes.home.home import home_bp
from app.routes.home.contact import contact_bp
from app.routes.home.about_me import about_bp
from app.routes.home.projects import projects_bp

def init_home(app: Flask):
    app.register_blueprint(home_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(projects_bp)