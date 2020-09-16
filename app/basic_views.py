# TODO: the search resolves multiples, but doesn't search by ID

from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
from flask import Flask, render_template, request

from app.bw_secrets import API_KEY
from app import basic_forms as bf
from app.helpers import print_weather_data

owm = OWM(API_KEY)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# the route handling the search query and form box
@app.route('/search_city', methods=['POST'])
def search_city():
    search_q: str = request.form['loc']

    if search_q == '':
        e = 'Field cannot be blank.'
        return render_template('index.html', error=e)

    try:
        manager = owm.weather_manager()
        observation = manager.weather_at_place(search_q)
    except NotFoundError:
        e = 'Entry not in registry. Please check your input.'
        return render_template('index.html', error=e)

    registry = owm.city_id_registry()
    multi = bf.format_multiples(registry, search_q)

    # in case of multiple cities with the same name are found
    if multi:
        e = 'There are many cities with that name. Try the city, country that matches best.'
        return render_template('index.html', multi=multi, error=e)
    else:
        # if single entry, then proceed with weather report
        info = bf.format_weather_data(observation)
        print_weather_data(info)
        return render_template('weather.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)
