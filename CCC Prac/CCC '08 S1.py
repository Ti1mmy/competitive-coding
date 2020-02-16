import sys
input = sys.stdin.readline
temp = 201
while 1:
    add = input()[:-1].split(" ")
    a = int(add[1])
    if a < temp:
        lowest = add[0]
        temp = a
    if 'Waterloo' in add:
        break
sys.stdout.write(lowest)
