import datetime, time, random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "trumpsucks"

@app.route('/')
def index():
	if (session.has_key('gold') == False) :
		session['gold'] = 0
	if (session.has_key('log') == False) :
		session['log'] = ""
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	if (request.form['building'] == 'farm'):
		reward = random.randrange(10,20)
		session['log'] = session['log'] + "\nEarned " + str(reward) + " golds from the farm! " + str(st)
	if (request.form['building'] == 'cave'):
		reward = random.randrange(5,10)
		session['log'] = session['log'] + "\nEarned " + str(reward) + " golds from the cave! " + str(st)
	if (request.form['building'] == 'house'):
		reward = random.randrange(2,5)
		session['log'] = session['log'] + "\nEarned " + str(reward) + " golds from the house! " + str(st)
	if (request.form['building'] == 'casino'):
		reward = random.randrange(-50,50)
		session['log'] = session['log'] + "\nEntered a casino for " + str(reward) + " golds! " + str(st)
	session['gold'] = session['gold'] + reward
	return redirect('/')

app.run(debug=True)
