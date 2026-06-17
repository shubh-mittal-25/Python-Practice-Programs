import os
import dotenv
import requests

dotenv.load_dotenv()
APP_ID = os.environ.get("EXERCISE_APP_ID")
API_KEY = os.environ.get("EXERCISE_API_KEY")
WEIGHT = 60
HEIGHT = 175
AGE = 22
GENDER = "male"

text = input("State your exercise : ")

endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
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
response = requests.post(endpoint, json=parameters, headers=header)
result = response.json()
print(result)
