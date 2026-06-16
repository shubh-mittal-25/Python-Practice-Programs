import requests
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
username = os.getenv("PIXELA_USERNAME")
graph_id = os.getenv("GRAPH_ID")
#-----------------------CREATE ACCOUNT---------------------------------------
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

#-----------------------CREATE GRAPH---------------------------------------
# graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
# print(username)
headers = {"X-USER-TOKEN": str(api_key)}
# graph_parameters = {
#     "id": graph_id,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }
#
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

#-----------------------POST VALUE TO GRAPH---------------------------------------
value_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
today = datetime.now()
today = today.strftime("%Y%m%d")

km:str = input("How many kilometers did you cycle today? : ")
parameters={
    "date": today,
    "quantity": km,
}

response = requests.post(value_endpoint, headers=headers, json=parameters)
print(response.text)

# #-----------------------UPDATE VALUE TO GRAPH---------------------------------------
#
# update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today}"
# new_data = {
#     "quantity": "6.8", }
#
# requests.put(update_endpoint, headers=headers, json=new_data)
#
# #-----------------------DELETE VALUE TO GRAPH---------------------------------------
# delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today}"
# requests.delete(delete_endpoint, headers=headers)