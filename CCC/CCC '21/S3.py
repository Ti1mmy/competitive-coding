from sys import stdin, stdout

friends = []
for i in range(int(stdin.readline())):
    friends.append([int(num) for num in stdin.readline().split(" ")])  # [deltaPos, sec/m, hearingdist]
print(friends)
distances = []
for friend in friends:
    distances.append(friend[0])
distances.sort()
lowest = -1
for i in range(distances[0], distances[-1] + 1):
    time = 0
    for friend in friends:
        timepos = abs(i - friend[0] + friend[2]) * friend[1]
        timeneg = abs(i - friend[0] - friend[2]) * friend[1]
        if timeneg < timepos:
            time += timeneg
        else:
            time += timepos
    if time < lowest or lowest == -1:
        lowest = time

stdout.write(str(lowest))
