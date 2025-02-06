from flask import Flask
from app.routes.home import init_home


def init_app(app: Flask):
    
    init_home(app)
   
