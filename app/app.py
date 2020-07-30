from flask import Flask
from flask import render_template
from flask import request
import json
import modelRunner
import os

MyApp = Flask(__name__,
              static_url_path='',
              static_folder='web',
              template_folder='web')


@MyApp.route('/')
def index():
    return render_template("index.html")

@MyApp.route('/checkUsername', methods = ['POST'])
def checkUsername():
    username = request.form.get('username')
    results = modelRunner.model(username)
    return str(results)

@MyApp.route('/userHistory')
def userHistory():
    return render_template("userHistory.html")


if __name__ == '__main__':
    #tester()
    MyApp.run(debug=True) # flask run -h 192.168.86.36    passenger:  from app import MyApp as application

print(os. getcwd())