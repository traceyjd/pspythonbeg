
#  Creating a weather app to get local weather data

import requests

def get_weather_desc_and_temp():
    api_key = "" # !!!!!  you will need to got to the url below and get API Key, then run program but dont commit to github, remove API Key first!!!!!!
    city = "Livingston"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description": description,
            "temp_min": temp_min,
            "temp_max": temp_max}


def main():
    weather_dict = get_weather_desc_and_temp()
    # Print Results
    print("Todays forecast is", weather_dict.get("description"))
    print("The minimum temperature is", weather_dict.get("temp_min"))
    print("The maximum temperature is", weather_dict.get("temp_max"))


main()

