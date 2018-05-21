# /usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
manage = Manager(app)
bootstrap = Bootstrap(app)
db=SQLAlchemy(app)
moment=Moment(app)


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/comments/<int:num>')
def comments(num):
    return render_template('comments.html', num=num)


if __name__ == '__main__':
    manage.run()
