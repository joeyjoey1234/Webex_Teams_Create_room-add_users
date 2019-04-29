import requests
auth_key= input("copy and paste your auth KEY:  ")
team_ID= input("copy and paste the team id you wish to create rooms for!   ")
room_title= input("Enter room name  ")

email_list = input("Copy and paste your distro list here")
email_list = email_list.replace('<',"")
email_list = email_list.replace('>',"")
email_list = email_list.replace(';',"")
email_list = email_list.split()

final_email_list = []
for x in email_list:
    if 'wwt.com' in x:
        final_email_list.append(x)


print(final_email_list)

url_create_room = 'https://api.ciscospark.com/v1/rooms'
url_add_users = 'https://api.ciscospark.com/v1/memberships'

headers = {'Authorization': 'Bearer {}'.format(auth_key),
           'Content-Type': 'application/json'}
data_createroom = {"title":"{}".format(room_title),"teamId":"{}".format(team_ID)}



create_room = requests.api.post(url=url_create_room,data=None,json=data_createroom,headers=headers)

room_id = create_room.text
room_id = str(room_id)
room_id = room_id.split(',',1)
room_id =room_id[0]
room_id = room_id.split('"')
room_id = room_id[3]
room_id = str(room_id)
print(room_id)

for x in final_email_list:
    data_adduser={"roomId":"{}".format(room_id),"personEmail":"{}".format(x)}
    add_users_to_room = requests.api.post(url=url_add_users,data=None,json=data_adduser,headers=headers)
    print(add_users_to_room.text)
