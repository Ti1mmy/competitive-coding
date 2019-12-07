list = []
newlist = []
planets = []
newplanets = []
points = []
seen = []
distance = 0
routes = []
count = 0
while True:
    x = input()
    if x == "":
        break
    else:
        list.append(x)
for orbit in list:
    newlist.append(orbit.split(")"))
for i in range(len(newlist)):
    for q in range(len(newlist[i])):
        if newlist[i][q] not in points:
            points.append(newlist[i][q])
root = 'COM'
points.remove(root)
for point in points:
    temp = []
    to_search = point
    while to_search != 'COM':
        for i in range(len(newlist)):
            if newlist[i][1] == to_search:
                temp.append(newlist[i][1])
                to_search = newlist[i][0]
    routes.append(temp)
for route in routes:
    route.reverse()
    count += len(route)
print(routes)
print(count)
