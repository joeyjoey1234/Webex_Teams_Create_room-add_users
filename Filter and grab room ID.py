import requests
from requests.auth import HTTPBasicAuth
auth_key= 'Fake cisco teams auth key'
team_ID= 'fake team ID'
room_title= 'here we go again'

url_create_room = 'https://api.ciscospark.com/v1/rooms'
headers = {'Authorization': 'Bearer {}'.format(auth_key),
           'Content-Type': 'application/json'}
data_createroom={"title":"{}".format(room_title),"teamId":"{}".format(team_ID)}


create_room = requests.api.post(url=url_create_room,data=None,json=data_createroom,headers=headers)

room_id = create_room.text
room_id = str(room_id)
room_id = room_id.split(',',1)
room_id =room_id[0]
room_id = room_id.split('"')
room_id = room_id[3]
room_id = str(room_id)
print(room_id)
