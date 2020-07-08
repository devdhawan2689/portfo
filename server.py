#!/usr/bin/python3
from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


def add_to_database(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')


def add_to_csv(data):
	with open('database.csv',newline='' ,mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	add_to_csv(data)
    	return redirect('/thankyou.html')

























# @app.route('/index.html')
# def home():
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')