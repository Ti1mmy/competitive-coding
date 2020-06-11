from sys import stdin, stdout
from itertools import permutations
a = list(stdin.readline())[:-1]
for i in sorted(permutations(a, len(a))):
    stdout.write(f'{"".join(i)}\n')