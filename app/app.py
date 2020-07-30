from flask import Flask
from flask import render_template
from flask import request
import json

MyApp = Flask(__name__,
              static_url_path='',
              static_folder='web',
              template_folder='web')


@MyApp.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    #tester()
    MyApp.run(debug=True) # flask run -h 192.168.86.36    passenger:  from app import MyApp as application