from flask import Flask
from flask import render_template
from flask import request
import json
import modelRunner
import os
import praw

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

reddit = praw.Reddit(client_id="j9QFz_ZMlTjxew", client_secret="Ujqus68T1uDq5q8blKyY7GmMmxM", user_agent="VD")
sender = smtplib.SMTP(host='smtp.mail.com', port=587)
sender.starttls()

email = "suicidewatch.hackathon@mail.com"
password = "suicidewatch.123"

sender.login(email, password)

MyApp = Flask(__name__,
              static_url_path='',
              static_folder='web',
              template_folder='web')


@MyApp.route('/')
def index():
    return render_template("index.html")

@MyApp.route('/checkUsername', methods = ['POST'])
def checkUsername():

    return str("results")

def readInfo(username):
    cmts = list(reddit.redditor(username).comments.new(limit=100))
    data = []
    for cmt in cmts:
        results = modelRunner.model(cmt.body)
        state = "regular"
        currMax = results[0]
        if(results[1] > currMax):
            currMax = results[1]
            state = "suicide"
        if(results[2] > currMax):
            currMax = results[2]
            state = "depression"
        data.append({"comment": cmt.body, "state": state, "prob": currMax, "urgent_warning": state=="suicide", "warning": state=="depression"})
    return data

def sendEmail(username, email_address):
    data = readInfo(username)
    # TODO: turn the json into an email
    msg = MIMEMultipart()
    msg['From'] = "suicidewatch.hackathon@mail.com"
    msg['To'] = email_address
    msg['Subject']= "SuicideWatch update on " + username
    msg.attach(MIMEText(data, 'plain'))

    sender.send_message(msg)

    del msg

@MyApp.route('/userHistory')
def userHistory():
    return render_template("userHistory.html")


if __name__ == '__main__':
    #tester()
    MyApp.run(debug=True) # flask run -h 192.168.86.36    passenger:  from app import MyApp as application

print(os. getcwd())