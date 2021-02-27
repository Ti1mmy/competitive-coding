from sys import stdin, stdout

rows = int(stdin.readline())
columns = int(stdin.readline())


visited = []
for i in range(int(stdin.readline())):
    brush = stdin.readline().split(" ")
    if brush[0] == "C": # True
        visited.append([int(brush[1]), True])
    else:
        visited.append([int(brush[1]), False])

visited_columns = []
visited_rows = []
b_intersections = []
g_intersections = []
for i in range(len(visited)):
    if visited[i][1]:
        for row in visited_rows:
            if [visited[i][0], row] in b_intersections:
                b_intersections.remove([visited[i][0], row])
                g_intersections.append([visited[i][0], row])
            else:
                b_intersections.append([visited[i][0], row])
        if visited[i][0] in visited_columns:
            visited_columns.remove(visited[i][0])
        else:
            visited_columns.append(visited[i][0])
    else:
        for column in visited_columns:
            if [column, visited[i][0]] in b_intersections:
                b_intersections.remove([column, visited[i][0]])
                g_intersections.append([column, visited[i][0]])
            else:
                b_intersections.append([column, visited[i][0]])
        if visited[i][0] in visited_rows:
            visited_rows.remove(visited[i][0])
        else:
            visited_rows.append(visited[i][0])

print(b_intersections)
print(g_intersections)
# gold = []
# for i in range(int(stdin.readline())):
#     brush = stdin.readline().split(" ")
#     if brush[0] == "C":
#         for row in range(rows):
#             pos = [int(brush[1]) - 1, row]
#             if pos in gold:
#                 gold.remove(pos)
#             else:
#                 gold.append(pos)
#     else:
#         for column in range(columns):
#             pos = [column, int(brush[1]) - 1]
#             if pos in gold:
#                 gold.remove(pos)
#             else:
#                 gold.append(pos)

print(len(b_intersections) + len(visited_columns) * rows + len(visited_rows) * columns)
print(visited_rows)
print(visited_columns)