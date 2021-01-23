import sys
input = sys.stdin.readline
month = int(input())
day = int(input())
if month <= 2:
    if day < 18 and month == 2:
        print('Before')
    elif month == 1:
        print('Before')
    elif day == 18:
        print('Special')
    else:
        print('After')
else:
    print('After')