import requests
import datetime

MY_LAT = 28.350215
MY_LONG = 79.423187

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json" , params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]

time_now = datetime.datetime.now()
print(time_now)
print(sunrise_time)
print(sunset_time)