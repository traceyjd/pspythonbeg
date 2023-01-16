
#  Creating a weather app to get local weather data

import requests

api_key = ""
city = "Livingston"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Todays forecast is", description)
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)

temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_max)

