def display_weather(obs) -> dict:
    info: dict = obs.to_dict()
    conversion = {
        'temperature': obs.weather.temperature(unit='fahrenheit'),
        'sunrise_time': obs.weather.sunrise_time(timeformat='date'),
        'sunset_time': obs.weather.sunset_time(timeformat='date'),
        'icon_url': obs.weather.weather_icon_url()
    }

    info.update(conversion)
    return info
