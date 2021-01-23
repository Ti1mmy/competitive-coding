a = int(input())
a2 = int(input())
a3 = int(input())
b = int(input())
b2 = int(input())
b3 = int(input())
a4 = a * 3 + a2 * 2 + a3
b4 = b * 3 + b2 * 2 + b3
if b4 > a4:
    print('B')
elif a4 > b4:
    print('A')
else:
    print('T')
