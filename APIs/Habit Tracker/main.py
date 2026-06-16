import requests
import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
user_name = os.getenv("USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"
# user_parameters = {
#     "token": api_key,
#     "username": user_name,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

