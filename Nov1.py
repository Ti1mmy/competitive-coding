import sys
input = sys.stdin.readline
mass = []
masssum = []
for i in range(int(input())):
    mass.append(int(input()))
for i in range(len(mass)):
    if i == 0:
        masssum.append(mass[i])
    else:
        masssum.append(masssum[i-1] + mass[i])
for i in range(int(input())):
    a = input()
    b = a.split()
    if b[0] == '0':
        print(masssum[int(b[1])])
    else:
        print(masssum[int(b[1])] - masssum[int(b[0])-1])
