from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/inq')
def inq():
    return render_template("inq.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")
