start_distro = input("please copy and paste distro from outlook   ")
distro = start_distro.replace('<',"")
distro = distro.replace('>',"")
distro = distro.replace(';',"")
distro = distro.split()

name_distro = []
email_distro = []
for x in distro:
    if '@' in x:
        email_distro.append(x)


names = start_distro.replace('<',"")
names = names.replace('>',"")
names = names.replace(';',"")
names = names.replace("@"," ")
names = names.split()

for x in names:
    if '.' in x and ".com" in x:
        pass
    elif '.' in x:
        name_distro.append(x)
    else:
        pass

email_distro.sort(key=str.lower)
cache = []


for x in email_distro:
    print(x)





