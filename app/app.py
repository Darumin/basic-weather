from pyowm import OWM, exceptions
from flask import Flask, render_template, request

API_KEY = 'a4d79ba5185e500e61b26adc39e08808'
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

    info = {}

    info['loc'] = l.get_name()
    info['loc_id'] = l.get_ID()

    info['stats'] = w.get_detailed_status()
    info['temp_cels'] = w.get_temperature('celsius')['temp']
    info['temp_fahr'] = w.get_temperature('fahrenheit')['temp']
    info['wind'] = w.get_wind(unit='meters_sec')['speed']
    info['wind_deg'] = w.get_wind()['deg']
    info['sunrise'] = w.get_sunrise_time(timeformat='iso')
    info['sunset'] = w.get_sunset_time(timeformat='iso')
    info['img_url'] = w.get_weather_icon_url()

    return info

if __name__ == '__main__':
    app.run(debug=True)
