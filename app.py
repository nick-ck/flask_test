# /usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>hello</h1>"
