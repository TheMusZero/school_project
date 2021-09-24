import requests

appid = 'a42fd268fcfa306dcb65da5c5b9c4a48'


def peek_cities(s_city):
    a = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

    data = a.json()
    count = 0
    cities = []
    for i in data["list"]:
        count += 1
        cities.append([count, i['name'], i['sys']['country'], i['id']])
    return cities


def weather(s_city):
    a = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

    data = a.json()
    print(data)
    main = data["main"]
    wind = data["wind"]

    temp = int(main["temp"])
    hum = int(main["humidity"])
    speed_of_wind = wind["speed"]
    pressure = int(main["pressure"])

    weather = str(data["weather"][0]["main"])

    return temp, hum, speed_of_wind, pressure, weather.lower()


def forecast(city_id):
    a = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                         params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = a.json()
    array = [[i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']),
              i['weather'][0]['description']] for i in data["list"]]
    return array
