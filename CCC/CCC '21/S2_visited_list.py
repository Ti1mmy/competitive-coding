from sys import stdin, stdout

rows = int(stdin.readline())
columns = int(stdin.readline())


gold = []
for i in range(int(stdin.readline())):
    brush = stdin.readline().split(" ")
    if brush[0] == "C":
        for row in range(rows):
            pos = [int(brush[1]) - 1, row]
            if pos in gold:
                gold.remove(pos)
            else:
                gold.append(pos)
    else:
        for column in range(columns):
            pos = [column, int(brush[1]) - 1]
            if pos in gold:
                gold.remove(pos)
            else:
                gold.append(pos)

stdout.write(str(len(gold)))