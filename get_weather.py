# Produce a python script that can accept a postcode as an argument and print out the current weather status for that postcode.
import sys
import requests
from pprint import pprint

POSTCODES_API = "https://api.postcodes.io/postcodes/"
WEATHER_API = "https://api.openweathermap.org/data/2.5/weather"


def main():
    # Join to Handle spaces between Spaces
    postcode = " ".join(sys.argv[1:])

    if postcode is "":
        print("Please enter a real postcode")
    
    # Load API key which is hidden
    with open("weather_api_key") as key:
        api_key = key.read().strip()

    # 1. Get latitude + longitude from postcode
    req = requests.get(POSTCODES_API + postcode.replace(" ", ""))
    data = req.json()["result"]
    # print(data)

    lat = data["latitude"]
    lon = data["longitude"]
    

    # 2. Get weather from OpenWeather
    weather = requests.get(
        WEATHER_API,
        params={
            "lat": lat,
            "lon": lon,
            "appid": api_key,
            "units": "metric"
        }
    ).json()
    pprint(weather)


    print("\nWeather for", postcode)
    print("Condition:", weather["weather"][0]["description"])
    print("Temperature:", weather["main"]["temp"], "°C")
    print("Feels like:", weather["main"]["feels_like"], "°C")


if __name__ == "__main__":
    main()


# List within list
# lists can be same data type or different con contains lists dictionary
big_list = [1, "hello",[1,2,3,[4,5,6]]]
# Will print [4,5,6]
print(big_list[2][3])



