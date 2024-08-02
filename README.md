# Weather_App

This is a Flask application that renders the current weather in a chosen city based on a free API from openweathermap.org

<div align="center">
    <img src="https://github.com/user-attachments/assets/981dac80-f259-481b-92c2-1ce7b8b003a3">
</div>

_First page gets input for city and unit of measurement_

<div align="center">
    <img src="https://github.com/user-attachments/assets/a32927ce-431f-43c8-8cfc-a0f134e6a2ca">
</div>

_Second page with API data_

## How to use
- Create an account on openweathermap.org and get your api_key from there
- Set up your development environment and install Flask
- Create your environment variables in .env file:
    - add a SECRET_KEY, random string which should be hard to guess
    - add your api_key
- python app.py to start server and run the app

## How it works
User inputs desired city and unit of measurement. Weather information (current weather description and temperature) is then displayed on a second page.

## Interesting app features
I enjoyed playing with my CSS abilities and created a sparkling button to generate weather data for chosen city and a dynamic background.

