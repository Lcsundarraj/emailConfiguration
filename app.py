from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import smtplib, ssl

from flask_mail import Mail,Message

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import email_db
import test

app= Flask(__name__)

mail =Mail(app)

@app.route('/')
def index():
	return render_template("emailConfiguration.html")

def setEmailInfo():
	email_info={}
	sender=request.form['sender']
	receiver=request.form['receiver']
	sub=request.form['sub']
	Message=request.form['Message']
	#send data ta List
	email_info['sender']=sender
	email_info['receiver']=receiver
	email_info['sub']=sub
	email_info['Message']=Message

	return email_info

@app.route('/', methods=['POST'])
def send_to_mail():
	email_info=setEmailInfo()
	test.send_mail(email_info)
	return redirect(url_for('configure_email'))



@app.route('/email',  methods=['POST'])
def configure_email():
	email_info=setEmailInfo()
	# print the list
	print("Sending Data to DB")
	print(email_info)
	email_db.save_email_info(email_info)
	return redirect(url_for('index'))



if __name__ == "__main__":
	app.run(debug=True)