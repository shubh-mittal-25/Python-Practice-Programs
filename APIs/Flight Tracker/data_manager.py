import os
import dotenv
from requests.auth import HTTPBasicAuth
import requests

dotenv.load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/b0f6d9080e2e5098265356b410516807/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

