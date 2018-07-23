# coding:utf8
# created at 2018/7/23.

from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import book