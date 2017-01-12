from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", phrase="Bion Rocks My Sox!!1", times=2, hello="hello")

app.run(debug=True)