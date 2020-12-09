import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "askdlfoiwssj3489alskdj89ajkg04jlauzlkx9g0a",
    "username": "rickgoshen",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
