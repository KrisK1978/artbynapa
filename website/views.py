from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


@views.route('/contact')
def contact():
    return render_template("contact.html")
