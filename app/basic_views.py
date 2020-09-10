from pyowm import OWM
from pyowm.exceptions import api_response_error as err

from flask import Flask, render_template, request

from app.bw_secrets import API_KEY
from app.basic_forms import display_weather

owm = OWM(API_KEY)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_city', methods=['POST'])
def search_city():
    location: str = request.form['loc']

    if location == '':
        e = 'Field cannot be blank.'
        return render_template('index.html', error=e)

    try:
        observation = owm.weather_at_place(location)
    except err.NotFoundError:
        e = 'Entry not in registry. Please check your input.'
        return render_template('index.html', error=e)

    info = display_weather(observation)
    return render_template('weather.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)
