import requests
from requests.auth import HTTPBasicAuth
auth_key= 'YzM0YWNhMmQtOGQ4OC00ZjVjLWFlZDYtYjNlZGNjNjk2YThjOWUxYTkxNTctYmFi_PF84_f88c9535-c5ce-4eb5-b166-be95180e4c32'
team_ID= 'Y2lzY29zcGFyazovL3VzL1RFQU0vYmY5NTQ4NTAtNmE4Zi0xMWU5LTljMTMtMzcwNDgzOWNjZTZj'
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
