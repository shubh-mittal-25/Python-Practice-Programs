import requests
import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
username = os.getenv("PIXELA_USERNAME")
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
# headers = {"X-USER-TOKEN": str(api_key)}
# graph_parameters = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }
#
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)


