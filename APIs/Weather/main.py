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
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(data)