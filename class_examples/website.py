import requests

if __name__ == '__main__':
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    r = requests.get(url)  # save the content of the url
    __data = r.json()
    print(__data["current_units"], "     ", ["time"])
    r = requests.get(
        "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1jhwk2.img?w=534&h=372&m=6&x=385&y=156&s=221&d=221")
    with open('likee.png', mode='wb') as what:
        what.write(r.content)
    # print(__data)
