import random
from flask import Flask, session, render_template, request, redirect

app = Flask(__name__)
app.secret_key = 'SecretSquirrelKey'

@app.route('/')
def index():
	session['alert'] = ""
	if session.has_key('number'):
		session.pop('number')
		session['number'] = random.randrange(0,101)
	elif (session.has_key('number')==False):
		session['number'] = random.randrange(0,101)
	if session.has_key('alert'):
		return render_template('index.html', alert=session['alert'])
	elif session.has_key('alert')==False:
		return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if (request.form['guess'] == False):
		return redirect('/')
	guess = int(request.form['guess'])
	number = int(session['number'])
	if (guess == number):
		session['alert'] = "you got it right!"
		return render_template('index.html', alert=session['alert'], number=session['number'])
	elif (guess > number):
		session['alert'] = "too high!"
	elif (guess < number):
		session['alert'] = "too low!"
	return render_template('index.html', alert=session['alert'], button=session['button'])

@app.route('/reset', methods=["POST"])
def reset():
	session.redirect('/')

app.run(debug=True)