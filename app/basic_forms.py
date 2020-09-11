def display_weather(obs) -> dict:
    info: dict = obs.to_dict()
    conversion: dict = {
        'temperature': obs.weather.temperature(unit='fahrenheit'),
        'sunrise_time': obs.weather.sunrise_time(timeformat='date'),
        'sunset_time': obs.weather.sunset_time(timeformat='date'),
        'icon_url': obs.weather.weather_icon_url()
    }

    info.update(conversion)
    return info


def format_multiples(regis, q):
    list_all: list = regis.locations_for(q)
    ret: list = list()

    if len(list_all) == 1: return False

    for entry in list_all:
        temp = f"{entry.name}, {entry.country} @ <lon:{entry.lon:.2f},"
        temp += f" lat:{entry.lat:.2f}> with ID: ({entry.id})"
        ret.append(temp)

    return ret
