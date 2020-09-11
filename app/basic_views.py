# TODO: the search resolves multiples, but doesn't search by ID

from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError

from flask import Flask, render_template, request

from app.bw_secrets import API_KEY
from app.basic_forms import display_weather, format_multiples

owm = OWM(API_KEY)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_city', methods=['POST'])
def search_city():
    manager = owm.weather_manager()
    registry = owm.city_id_registry()
    search_q: str = request.form['loc']

    if search_q == '':
        e = 'Field cannot be blank.'
        return render_template('index.html', error=e)

    try:
        observation = manager.weather_at_place(search_q)
    except NotFoundError:
        e = 'Entry not in registry. Please check your input.'
        return render_template('index.html', error=e)

    dupes = format_multiples(registry, search_q)

    if dupes:
        e = 'There are many cities with that name. Try the city, country that matches best.'
        return render_template('index.html', multi=dupes, error=e)

    info = display_weather(observation)
    return render_template('weather.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)
