import requests
auth_key= input("copy and paste your auth KEY:  ")
room_title= input("Enter room name  ")
####This takes the distro from a OUTLOOK TO FIELD and formats it so it can be injected later into a request
### also a print distro for debug final filter
email_list = input("Copy and paste your distro list here  ")
email_list = email_list.replace('<',"")
email_list = email_list.replace('>',"")
email_list = email_list.replace(';',"")
email_list = email_list.split()

final_email_list = []
for x in email_list:
    if '@' in x:
        final_email_list.append(x)


print("Here is your distro list {}".format(final_email_list))
######
####URls and headers for all requests made
url_create_room = 'https://api.ciscospark.com/v1/rooms'
url_add_users = 'https://api.ciscospark.com/v1/memberships'
url_list_teams = 'https://api.ciscospark.com/v1/teams'

headers = {'Authorization': 'Bearer {}'.format(auth_key),
           'Content-Type': 'application/json'}
####
### This block of code, requests users list of Team, and displays them to be choosen, to create a room in
list_room = requests.api.get(url=url_list_teams,data=None,json='{}',headers=headers)
list_room_filter = list_room.text
list_room_filter = list_room_filter.replace('{','')
list_room_filter = list_room_filter.replace('}','')
list_room_filter = list_room_filter.replace('[','')
list_room_filter = list_room_filter.replace('items','')
#list_room_filter = list_room_filter.replace(',',' ')
list_room_filter = list_room_filter.replace('"','')
list_room_filter = list_room_filter.split(',')
name_list = []
id_list = []

for x in list_room_filter:
    if 'name' in x:
        name_list.append(x.replace('name:',''))
    elif 'id' in x:
        x = x.replace(':id:','')
        id_list.append(x.replace('id:',''))

options_rooms = dict(zip(name_list, id_list))

for k in options_rooms:
    print(k)
key_select = input("please type in TEAM name you wish to use or leave blank for no team selection  ")
final_key = options_rooms[key_select]
#####
data_createroom = {"title":"{}".format(room_title),"teamId":"{}".format(final_key)}
##### Grabs newly created room ID number, to add users in a later function
create_room = requests.api.post(url=url_create_room,data=None,json=data_createroom,headers=headers)

room_id = create_room.text
room_id = str(room_id)
room_id = room_id.split(',',1)
room_id = room_id[0]
room_id = room_id.split('"')
room_id = room_id[3]
room_id = str(room_id)
print("This is your new room ID :  {}".format(room_id))
####Debug for new room id
##
### This for loop runs through final_email_list to add users to just created room_id
for x in final_email_list:
    data_adduser={"roomId":"{}".format(room_id),"personEmail":"{}".format(x)}
    add_users_to_room = requests.api.post(url=url_add_users,data=None,json=data_adduser,headers=headers)
    print("debug: adding user {} :: {}".format(x,add_users_to_room.text))
