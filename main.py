import json
import requests

URL = "https://restroomtempv2.azurewebsites.net/api/RoomTemp"

id = 2
# if data cant get serialized properly using the data= method then use json=
# json tell the webservice directly that im using json
# by sending the application/json header
# whilst data uses the application/x-www-form-urlencoded header
# which tells the webservice to encode the data in the url or body
payload = {
    "Id": 6,
    "RoomNo": "D2.14",
    "Temp": 14,
    "Day": "Sunday"
}


response = requests.get(URL)
format_json = response.json()
print(format_json)
id_response = requests.get(URL + "/" + f"{id}")
format_json_id = id_response.json()
print(format_json_id)
post_response = requests.post(URL, json=payload)
post_response_to_json = post_response.json()
print(post_response_to_json)