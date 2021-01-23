input = sys.stdin.readline
a = input()
x = []
for i in a:
    x.append(i)
x.pop()
l = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
possible = True
for b in x:
    if b not in l:
        possible = False
if possible:
    print('YES')
else:
    print('NO')