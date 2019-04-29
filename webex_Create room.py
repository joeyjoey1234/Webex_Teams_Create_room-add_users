import requests
from requests.auth import HTTPBasicAuth
auth_key= input("please copy your api auth key")
team_ID= input("please copy and paste your team ID")
room_title= input("What is the room title? ")

url_create_room = 'https://api.ciscospark.com/v1/rooms'
headers = {'Authorization': 'Bearer {}'.format(auth_key),
           'Content-Type': 'application/json'}
data={"title":"{}".format(room_title),"teamId":"{}".format(team_ID)}


create_room = requests.api.post(url=url_create_room,data=None,json=data,headers=headers)

