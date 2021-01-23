from sys import stdin
input = stdin.readline
msmts = []
flowers = int(input())
for i in range(flowers):
    msmts.append([int(num) for num in input().split(" ")])


def rotate90(list):
    newlist = [[] for _ in range(len(list))]
    for v in range(len(list[0])):
        for c in range(len(list)):
            newlist[c].insert(0, list[v][c])
    return newlist


def possible(list):
    possible_msmts = []
    for i in range(4):
        count = 0
        for k in range(flowers):
            if list[k] == sorted(list[k]):
                count += 1
        if count == flowers:
            possible_msmts.append(list)
        list = rotate90(list)
    return possible_msmts


possible_measurements = possible(msmts)

for i in range(len(possible_measurements)):
    tmp = [[], []]
    for g in possible_measurements[i]:
        tmp[0].append(g[0])
        tmp[1].append(g[-1])
    if tmp[0] == sorted(tmp[0]) and tmp[1] == sorted(tmp[1]):
        for out in possible_measurements[i]:
            print(" ".join(str(o) for o in out))
        break