# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'hogehoge'


if __name__ == '__main__':
    app.run()
