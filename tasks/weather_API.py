# //*[@id="Personality"]/div/div/span
# //*[@id="Personality"]/div/h4
# import requests

# with open('E:\Python\Tasks\pic.png', 'wb') as pic_file:
#     pic_file.write(requests.get('https://api.adorable.io/avatars/40/101.png').content)

# Home task:
# current weather in current location
# https://github.com/toddmotto/public-apis


import requests, json


appid = '66145595e759076a14b2f159e34a0e72'


def get_current_location():
    loc_lst = json.loads(requests.get('http://ipinfo.io/').content)['loc'].split(',')
    return {'lat': loc_lst[0], 'lon': loc_lst[1]}


def get_weather_by_coord(lat, lon, appid):
    weather_link = 'http://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={appid}'.format(
        lat=lat, lon=lon, appid=appid)
    return json.loads(requests.get(weather_link).content)


def cardinal_wind(direct):
    if direct > 348.75 or direct <= 11.25:
        return 'N'
    elif 11.25 < direct <= 33.75:
        return 'NNE'
    elif 33.75 < direct <= 56.25:
        return 'NE'
    elif 56.25 < direct <= 78.75:
        return 'ENE'
    elif 78.75 < direct <= 101.25:
        return 'E'
    elif 101.25 < direct <= 123.75:
        return 'ESE'
    elif 123.75 < direct <= 146.25:
        return 'SE'
    elif 146.25 < direct <= 168.75:
        return 'SSE'
    elif 168.75 < direct <= 191.25:
        return 'S'
    elif 191.25 < direct <= 213.75:
        return 'SSW'
    elif 213.75 < direct <= 236.25:
        return 'SW'
    elif 236.25 < direct <= 258.75:
        return 'WSW'
    elif 258.75 < direct <= 281.25:
        return 'W'
    elif 281.25 < direct <= 303.75:
        return 'WNW'
    elif 303.75 < direct <= 326.25:
        return 'NW'
    elif 326.25 < direct <= 348.75:
        return 'NNW'
    else:
        raise ValueError('degrees are to be in range [0, 360]')


def pretty_weather(verbosity):
    """
    verbosity == 0: city name, temperature
    verbosity == 1: city name, temperature, description, wind
    verbosity == 2: + humidity, pressure
    """
    location = get_current_location()
    weather = get_weather_by_coord(location['lat'], location['lon'], appid)
    weather_str = ''
    weather_str += '{}, '.format(weather['name'])
    weather_str += '{:5.1f}°C'.format(weather['main']['temp'])
    if verbosity >= 1:
        weather_str += ', {}'.format(weather['weather'][0]['description'])
        try:
            weather_str += ', wind {direct}, {speed:4.1f} m/s'.format(
                direct=cardinal_wind(weather['wind']['deg']),
                speed=weather['wind']['speed']
            )
        except KeyError:
            weather_str += ', wind {speed:4.1f} m/s'.format(
                speed=weather['wind']['speed']
            )
    if verbosity >= 2:
        weather_str += ', {}% humidity'.format(weather['main']['humidity'])
        weather_str += ', {} hPa'.format(weather['main']['pressure'])
        weather_str += ', {}% of cloud coverage'.format(weather['clouds']['all'])
    return weather_str


if __name__ == '__main__':
    print(pretty_weather(2))
