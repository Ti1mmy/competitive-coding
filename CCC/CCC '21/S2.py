from sys import stdin, stdout

rows = int(stdin.readline())
columns = int(stdin.readline())

painting = [[-1 for _ in range(columns)] for _ in range(rows)]
for i in range(int(stdin.readline())):
    brush = stdin.readline().split(" ")
    if brush[0] == "C":
        for k in range(rows):
            painting[k][int(brush[1])-1] *= -1
    else:
        for l in range(columns):
            painting[int(brush[1])-1][l] *= -1

gold = 0
for row in painting:
    gold += row.count(1)
stdout.write(str(gold))