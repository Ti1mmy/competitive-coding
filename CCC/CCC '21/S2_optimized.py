from sys import stdin, stdout

rows = int(stdin.readline())
columns = int(stdin.readline())


painting = [-1 for _ in range(columns * rows)]

for i in range(int(stdin.readline())):
    brush = stdin.readline().split(" ")
    if brush[0] == "C":
        for k in range(rows):
            painting[int(brush[1]) - 1 + k * columns] *= -1
    else:
        for l in range(columns):
            painting[(int(brush[1]) - 1) * columns + l] *= -1

stdout.write(str(painting.count(1)))