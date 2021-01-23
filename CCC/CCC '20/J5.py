import sys
input = sys.stdin.readline
m = int(input()[:-1])
n = int(input()[:-1])
data_old = []
for i in range(m):
    data_old.append(input()[:-1])
data = [d.split() for d in data_old]
for d in data:
    for i in range(len(d)):
        d[i] = int(d[i])
x = 0
y = 0 # Search yth list first, then find xth element in str to get element at (x, y)
keep_going = True
possible = False
flip = 0
hnng = True
if data[0][0] == 1:
    print('no')
else:
    while hnng:
        keep_going = True
        for i in range(n): # y
            for l in range(m): # x
                if keep_going:
                    if i == n - 1 and l == m - 1:
                        hnng = False
                        break
                    # print(i, l, (i + 1) * (l + 1), data[y][x], y, x, m, n) # (y, x)
                    if (i + 1) * (l + 1) == data[y][x]:
                        if flip % 2 == 0:
                            x = l
                            y = i
                        else:
                            x = i
                            y = l
                        keep_going = False
                        flip += 1
        if data[y][x] == m * n:
            possible = True
            break
    if possible:
        print('yes')
    else:
        print('no')
"""
3
4
3 10 8 14
1 11 12 12
6 2 3 9
"""
"""
3 m
4 n
3 10 8 14
1 11 12 12
6 2 3 9
"""