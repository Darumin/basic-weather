def print_weather_data(observation_dict):
    if 'weather' in observation_dict:
        weather_dict = observation_dict['weather']
    else: return

    for key, value in weather_dict.items():
        print(f"{key} --> {value}")