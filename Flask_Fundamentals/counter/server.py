from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key= 'SecretSquirrelKey'


@app.route('/')
def index():
	if session.has_key('times'):
		session['times'] = session['times'] + 1
	elif session.has_key('times')==False:
		session['times'] = 1
	return render_template('index.html', times=session['times'])


@app.route('/two')
def two():
	session['times'] = session['times'] + 1
	return redirect('/')

@app.route('/reset')
def reset():
	session['times'] = 0
	return redirect('/')

app.run(debug=True)