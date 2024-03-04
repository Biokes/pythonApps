import requests

if __name__ == '__main__':
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    r = requests.get(url)  # save the content of the url
    __data = r.json()
    print(__data["current_units"], "     ",["time"])
    # print(__data)
