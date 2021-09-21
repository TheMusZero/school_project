import requests


def weather(s_city):
    id = 'a42fd268fcfa306dcb65da5c5b9c4a48'
    a = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': id})

    data = a.json()
    if data['message'] == 'bad query':
        return 'bad_query'
    main = data["list"][0]["main"]
    wind = data["list"][0]["wind"]

    temp = int(main["temp"])
    hum = int(main["humidity"])
    speed_of_wind = wind["speed"]
    pressure = int(main["pressure"])

    weather = str(data["list"][0]["weather"][0]["main"])

    return temp, hum, speed_of_wind, pressure, weather.lower()
