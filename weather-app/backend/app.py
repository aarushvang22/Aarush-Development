from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///weather.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Current(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100))
    country = db.Column(db.String(100))
    region = db.Column(db.String(100))
    temp_c = db.Column(db.Float)
    temp_f = db.Column(db.Float)
    condition = db.Column(db.String(100))
    wind_mph = db.Column(db.Float)
    wind_dir = db.Column(db.String(100))
    humidity = db.Column(db.Integer)
    pressure = db.Column(db.Float)

class Forecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maxtemp_f = db.Column(db.Float)
    mintemp_f = db.Column(db.Float)
    avgtemp_f = db.Column(db.Float)
    maxwind_mph = db.Column(db.Float)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current", methods=["GET"])
def current():
    location = request.args.get("location", "")
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.route("/forecast", methods=["GET"])
def forecast():
    location = request.args.get("location", "")
    days = request.args.get("days", type=int)
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days={days}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.route("/currentdata", methods=["POST"])
def current_data():
    location = request.form["location"]
    country = request.form["country"]
    region = request.form["region"]
    temp_c = request.form["temp_c"]
    temp_f = request.form["temp_f"]
    conditon = request.form["condition"]
    wind_mph = request.form["wind_mph"]
    wind_dir = request.form["wind_dir"]
    humidity = request.form["humidity"]
    pressure = request.form["pressure"]
    weather_data = Current(location=location, country=country, region=region, temp_c=temp_c, temp_f=temp_f, conditon=conditon, wind_mph=wind_mph, wind_dir=wind_dir, humidity=humidity, pressure=pressure)
    db.session.add(weather_data)
    db.session.commit()
    return redirect("/results")

@app.route("/forecastdata", methods=["POST"])
def forecast_data():
    maxtemp_f = request.form["maxtemp_f"]
    mintemp_f = request.form["mintemp_f"]
    avgtemp_f = request.form["avgtemp_f"]
    maxwind_mph = request.form["maxwind_mph"]
    weather_data = Forecast(maxtemp_f=maxtemp_f, mintemp_f=mintemp_f, avgtemp_f=avgtemp_f, maxwind_mph=maxwind_mph)
    db.session.add(weather_data)
    db.session.commit()
    return redirect("/results")

@app.route("/results")
def results():
    current_weather_data = Current.query.all()
    forecast_weather_data = Forecast.query.all()
    return render_template("result.html", current_weather_data=current_weather_data, forecast_weather_data=forecast_weather_data)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
