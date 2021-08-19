from flask import render_template, url_for, flash, redirect
from demo import app
from demo.models import User, Post


@app.route("/")
def home():
    return render_template("home.html")
