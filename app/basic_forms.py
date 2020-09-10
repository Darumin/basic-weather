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