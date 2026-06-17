import os
import dotenv
import requests
from datetime import datetime

dotenv.load_dotenv()
APP_ID = os.environ.get("EXERCISE_APP_ID")
API_KEY = os.environ.get("EXERCISE_API_KEY")
sheety_api_key = os.environ.get("SHEETY_API_KEY")
WEIGHT = 60
HEIGHT = 175
AGE = 22
GENDER = "male"

text = input("State your exercise : ")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
header = {
    "x-app-id": str(APP_ID),
    "x-app-key": str(API_KEY),
}
parameters = {
    "query": text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
    }
response = requests.post(exercise_endpoint, json=parameters, headers=header)
result = response.json()
print(result)

sheety_endpoint = f"https://api.sheety.co/{sheety_api_key}/workoutTracking/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
for exercise in result["exercises"]:
    sheet_parameters = {
        "workout" : {
            "date" : today_date,
            "time" : time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }

sheety_response = requests.post(sheety_endpoint, json=sheet_parameters)

print(sheety_response.text)

# Supported activities:
#
# Running/Jogging - "ran for 30 minutes", "jogged 2 miles"
# Swimming - "swam for 1 hour", "swimming laps"
# Walking - "walked 3 miles", "brisk walk 45 min"
# Cycling - "biked for 1 hour", "rode bike 10 miles"
# Weightlifting - "lifted weights 45 min", "weight training"