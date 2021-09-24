import requests


def peek_cities(s_city):
    id = 'a42fd268fcfa306dcb65da5c5b9c4a48'
    a = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': id})

    data = a.json()
    count = 0
    cities = []
    for i in data["list"]:
        count += 1
        cities.append([count, i['name'], i['sys']['country'], i['id']])
    return cities


def weather(s_city):
    id = 'a42fd268fcfa306dcb65da5c5b9c44a8'
    a = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': s_city, 'type': 'like', 'units': 'metric', 'APPID': id})

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


def forecast(s_city):
    pass

def wanna_peek(number):
    a = peek_cities
