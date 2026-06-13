import requests
import os
import dotenv

dotenv.load_dotenv()
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
app_key = os.getenv("APP_KEY")

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": app_key,
    "cnt": 8,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

print("WEATHER")
for i in range(8):
    print(f"Date/Time: {weather_data['list'][i]['dt_txt']} | "
          f"Temperature: {round(weather_data['list'][i]['main']['temp'] - 273.15 , 2)} | "
          f"Feels Like: {round(weather_data['list'][i]['main']['feels_like'] - 273.15 , 2)} | "
          f"Humidity: {weather_data['list'][i]['main']['humidity']}% | "
          f"Wind Speed: {weather_data['list'][i]['wind']['speed']} m/s | "
          f"{weather_data["list"][i]["weather"][0]["main"]} | "
          f"{weather_data["list"][i]["weather"][0]["description"]}")
