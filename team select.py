import requests

auth_key= 'YzM0YWNhMmQtOGQ4OC00ZjVjLWFlZDYtYjNlZGNjNjk2YThjOWUxYTkxNTctYmFi_PF84_f88c9535-c5ce-4eb5-b166-be95180e4c32'

url_list_teams = 'https://api.ciscospark.com/v1/teams'

headers = {'Authorization': 'Bearer {}'.format(auth_key),
           'Content-Type': 'application/json'}




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
key_select = input("please type in TEAM name you wish to use leave blank for no team  ")
final_key = options_rooms[key_select]
