
import requests
api_key = "fb1a5654dbeda7dacb0c4ca2077ae634"
city = "Edinburgh"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

request = requests.get(url)
json = request.json()
print(json)