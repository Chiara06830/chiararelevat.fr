from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/experiences")
def experiences():
    return render_template("experiences.html")

@app.route("/education")
def education():
    return render_template("education.html")