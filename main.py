import requests
from datetime import datetime

USERNAME = "rickgoshen"
TOKEN = "askdlfoiwssj3489alskdj89ajkg04jlauzlkx9g0a"
PIXELA_ENDPOINT = "https://pixe.la/v1/users/"
GRAPH_ID = "graph1"
today = datetime.now()

# create user
user_endpoint = f"{PIXELA_ENDPOINT}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create a pixels graph
graph_endpoint = f"{PIXELA_ENDPOINT}{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Minutes Coding",
    "unit": "mins",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

# create a new pixel on habit graph
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code? ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response)

# update a pixel on habit graph
date_input = input("Enter in the date you would like to edit. (YYYYMMDD)")

pixel_update_endpoint = f"{PIXELA_ENDPOINT}{USERNAME}/graphs/{GRAPH_ID}/{date_input}"

update_data = {
    "quantity": pixel_data["quantity"]
}

response = requests.put(url=pixel_update_endpoint, json=update_data, headers=headers)
print(response.text)
