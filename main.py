import requests

USERNAME = "rickgoshen"
TOKEN = "askdlfoiwssj3489alskdj89ajkg04jlauzlkx9g0a"
PIXELA_ENDPOINT = "https://pixe.la/v1/users/"

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
    "id": "graph1",
    "name": "Minutes Coding",
    "unit": "mins",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)


