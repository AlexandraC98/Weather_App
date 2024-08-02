from flask import Flask, render_template, request, flash, redirect # type: ignore
from dotenv import load_dotenv # type: ignore
import requests # type: ignore
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
api_key = os.getenv('api_key')

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'


@app.route('/', methods=["POST","GET"])
def index():

    if request.method == 'POST':

        city = request.form.get("city").capitalize()
        units = request.form.get("units", "metric")

        if not city:
            flash ("City is required.")
            return redirect ('/')

        response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&APPID={api_key}")

        if response.status_code != 200:
            flash ("API couldn't load.")
            return redirect ('/404')
        
        weather_data = response.json()

        weather_description = weather_data["weather"][0]["description"].lower()
        temp = round(weather_data["main"]["temp"])

        return render_template(
            "weather.html",
            city=city,
            weather_description=weather_description,
            temp=temp,
            units=units
        )
    
    return render_template ("index.html")


@app.route ('/404')
def err():
    return render_template("err.html")


if __name__ == '__main__':
  app.run(debug=True)
