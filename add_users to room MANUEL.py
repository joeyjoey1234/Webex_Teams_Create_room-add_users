import requests
from requests.auth import HTTPBasicAuth
auth_key= input("input auth key  ")
url_create_room = 'https://api.ciscospark.com/v1/rooms'
room_id = input("please inpute room ID ")
headers = {'Authorization': 'Bearer {}'.format(auth_key),
           'Content-Type': 'application/json'}




### Everything under here is new
### create a func to find the just created room ID




url_add_users = 'https://api.ciscospark.com/v1/memberships'
distro = input("please inpute your distro list from out look:   ")
distro = distro.replace('<',"")
distro = distro.replace('>',"")
distro = distro.replace(';',"")
distro = distro.split()


final_distro = []
for x in distro:

    if '@' in x:
        final_distro.append(x)





for x in final_distro:
    data_adduser = {"roomId": "{}".format(room_id), "personEmail": "{}".format(x)}
    add_users_to_room = requests.api.post(url=url_add_users, data=None, json=data_adduser, headers=headers)

