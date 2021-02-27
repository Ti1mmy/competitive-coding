from sys import stdin, stdout

m = int(stdin.readline())
n = int(stdin.readline())
adjectives = []
nouns = []

for _ in range(m):
    adjectives.append(stdin.readline().strip())
for _ in range(n):
    nouns.append(stdin.readline().strip())

for adjective in adjectives:
    for noun in nouns:
        stdout.write(f'{adjective} as {noun}\n')