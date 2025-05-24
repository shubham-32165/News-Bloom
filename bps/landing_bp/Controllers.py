from flask import render_template, make_response
from .utility import weatherUtility

def index():
    weather_data = weatherUtility()
    return render_template("HomePage/landing.jinja.html", weather_data = weather_data )