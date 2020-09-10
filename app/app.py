from app.bw_secrets import API_KEY

from pyowm import OWM
from flask import Flask, render_template, request

owm = OWM(API_KEY)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_city', methods=['POST'])
def search_city():
    if request.form['loc'] == '':
        return render_template('index.html', error='Query cannot be blank.')
    else:
        try:
            loc = request.form['loc']
            obs = owm.weather_at_place(str(loc))
        except:
            return render_template('index.html', error='City not found.')
        else:
            info = display_weather(obs)
            return render_template('weather.html', info=info)


def display_weather(obs):
    w = obs.get_weather()
    l = obs.get_location()

    info: dict = {
        'loc': l.get_name(),
        'loc_id': l.get_ID(),
        'stats': w.get_detailed_status(),
        'temp_cels': w.get_temperature('celsius')['temp'],
        'temp_fahr': w.get_temperature('fahrenheit')['temp'],
        'wind': w.get_wind(unit='meters_sec')['speed'],
        'wind_deg': w.get_wind()['deg'],
        'sunrise': w.get_sunrise_time(timeformat='iso'),
        'sunset': w.get_sunset_time(timeformat='iso'),
        'img_url': w.get_weather_icon_url()
    }

    return info


if __name__ == '__main__':
    app.run(debug=True)
