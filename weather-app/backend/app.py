from flask import Flask, redirect, render_template, request

import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/current", methods=["GET"])
def current():
    location = request.args.get("location", "").strip()
    if not location:
        return render_template("index.html", error="Please enter a location.")

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"
    r = requests.get(url, timeout=15)
    data = r.json()

    if "error" in data:
        msg = data["error"].get("message", "Could not fetch weather.")
        return render_template("index.html", error=msg)

    loc = data.get("location", {})
    cur = data.get("current", {})

    payload = {
        "location_name": loc.get("name", location),
        "region": loc.get("region", ""),
        "country": loc.get("country", ""),
        "last_updated": cur.get("last_updated", "just now"),
        "temp_c": round(float(cur.get("temp_c", 0))),
        "feelslike_c": round(float(cur.get("feelslike_c", 0))),
        "condition_text": cur.get("condition", {}).get("text", "N/A"),
        "icon_url": ("https:" + cur.get("condition", {}).get("icon", "")) if cur.get("condition") else "",
        "humidity": cur.get("humidity", 0),
        "wind_kph": cur.get("wind_kph", 0),
    }
    return render_template("result.html", **payload)


@app.route("/forecast", methods=["GET"])
def forecast():
    location = (request.args.get("location") or "").strip()
    days_param = request.args.get("days", type=int) or 3  # default 3

    if not location:
        return render_template("index.html", error="Please enter a location for forecast.")
    if days_param < 1 or days_param > 10:
        return render_template("index.html", error="Days must be between 1 and 10.")

    url = "http://api.weatherapi.com/v1/forecast.json"
    r = requests.get(url, params={
        "key": API_KEY,
        "q": location,
        "days": days_param,
        "aqi": "no",
        "alerts": "no"
    }, timeout=15)
    data = r.json()

    # Handle API errors
    if "error" in data:
        msg = data["error"].get("message", "Could not fetch forecast.")
        return render_template("index.html", error=msg)

    loc = data.get("location", {}) or {}
    forecast_days = (data.get("forecast", {}) or {}).get("forecastday", []) or []

    # Build normalized list of days for the template
    days_payload = []
    for d in forecast_days:
        day = d.get("day", {}) or {}
        astro = d.get("astro", {}) or {}
        cond = (day.get("condition", {}) or {})

        days_payload.append({
            "date": d.get("date", ""),
            "maxtemp_c": round(float(day.get("maxtemp_c", 0))),
            "mintemp_c": round(float(day.get("mintemp_c", 0))),
            "avgtemp_c": round(float(day.get("avgtemp_c", 0))),
            "maxwind_kph": day.get("maxwind_kph", 0),
            "avghumidity": day.get("avghumidity", 0),
            "daily_chance_of_rain": day.get("daily_chance_of_rain", 0),
            "condition_text": cond.get("text", "N/A"),
            "icon_url": ("https:" + cond.get("icon", "")) if cond.get("icon") else "",
            "sunrise": astro.get("sunrise", ""),
            "sunset": astro.get("sunset", ""),
        })

    payload = {
        "query_location": location,
        "location_name": loc.get("name", location),
        "region": loc.get("region", ""),
        "country": loc.get("country", ""),
        "days": days_param,
        "days_payload": days_payload,
    }

    return render_template("forecast.html", **payload)


if __name__ == "__main__":
    app.run()
