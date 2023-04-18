import pixela as pixela
import requests
from datetime import datetime

USERNAME="annamani"
TOKEN="sfdhgsd798jlk2923b021"
GRAPH_ID="graph1"
TODAY=datetime.now().strftime("%Y%m%d")
print(TODAY)

pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response=requests.post(url=pixela.endpoint,json=user_params)
# print(response.text)
graph_params={
    "id":GRAPH_ID,
    "name":"Walking Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN
}
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(graph_response.text)

#posting a pixel in the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": TODAY,
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)