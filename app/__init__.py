# coding:utf8
# created at 2018/7/23.
from flask import Flask

def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)