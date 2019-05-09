distro = 'Penafiel, Jose <Jose.Penafiel@wwt.com>; Alsebei, Safwan <Safwan.Alsebei@wwt.com>; Brooks, Brittany <Brittany.Brooks@wwt.com>; Crist, Darius <Darius.Crist@wwt.com>; Dolinac, Zeljko <Zeljko.Dolinac@wwt.com>; Duran, Rosie <Rosie.Duran@wwt.com>; Erickson, Brian <Brian.Erickson@wwt.com>; Gibson, Geoffrey <Geoffrey.Gibson@wwt.com>; Harrington, Terri <Terri.Harrington@wwt.com>; Heber, Colton <Colton.Heber@wwt.com>; Hudson, Terra <Terra.Hudson@wwt.com>; LeBrun, Bryan <Bryan.LeBrun@wwt.com>; Medina, Julio <Julio.Medina@wwt.com>; Mulvanity, Ryon <Ryon.Mulvanity@wwt.com>; Narayan, Asheel <Asheel.Narayan@wwt.com>; Pass, Vic <Vic.Pass@wwt.com>; Penafiel, Jose <Jose.Penafiel@wwt.com>; Robinson, Joe <Joe.Robinson@wwt.com>; Smith, Francis <Francis.Smith@wwt.com>; Smith, Tamica <Tamica.Smith@wwt.com>; Strange, Chase <Chase.Strange@wwt.com>; Torres, Jonnie <Jonnie.Torres@wwt.com>; Valdez, Michelle <Michelle.Valdez@wwt.com>; Van Maanen, Eric <Eric.VanMaanen@wwt.com>; Warren, Justin <Justin.Warren@wwt.com>'
distro = distro.replace('<',"")
distro = distro.replace('>',"")
distro = distro.replace(';',"")
distro = distro.split()


final_distro = []
for x in distro:

    if '@' in x:
        final_distro.append(x)



for x in final_distro:
    print(x)
