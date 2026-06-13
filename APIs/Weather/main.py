import requests
import os
import dotenv
import random
import smtplib

dotenv.load_dotenv()
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
app_key = os.getenv("APP_KEY")
sender = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver = os.getenv("RECEIVER_EMAIL")

with open("quotes.txt") as file:
    quotes = file.readlines()
today_quote = random.choice(quotes)

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": app_key,
    "cnt": 8,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
print(f"Sunrise: {sunrise} | Sunset: {sunset}")

print("WEATHER")
today = ""
for i in range(8):
    forecast = weather_data['list'][i]
    today += (
        f"Date/Time: {forecast['dt_txt']} | "
        f"Temperature: {forecast['main']['temp'] - 273.15:.2f} C | "
        f"Feels Like: {forecast['main']['feels_like'] - 273.15:.2f} C | "
        f"Humidity: {forecast['main']['humidity']}% | "
        f"Wind Speed: {forecast['wind']['speed']} m/s | "
        f"{forecast['weather'][0]['main']} | "
        f"{forecast['weather'][0]['description']}\n\n"
    )

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(
        from_addr=sender,
        to_addrs=sender,
        msg=(
            f"Subject: Daily Notification\n\n"
            f"{today_quote}\n\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}\n\n"
            f"{today}"
        )
    )

