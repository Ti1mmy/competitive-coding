coords = []
for i in range(int(input())):
    coords.append(input())
x = []
y = []
t = []
for i in range(len(coords)):
    t.append(coords[i].split(","))
for i in range(len(t)):
    x.append(int(t[i][0]))
    y.append(int(t[i][1]))
x.sort()
y.sort()
print(f"{x[0] - 1},{y[0] - 1}")
print(f"{x[-1] + 1},{y[-1] + 1}")
