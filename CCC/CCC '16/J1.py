import sys
input = sys.stdin.readline
results = []
for i in range(6):
    results.append(input().rstrip())
if results.count('W') > 4:
    print(1)
elif results.count('W') > 2:
    print(2)
elif results.count('W') > 0:
    print(3)
else:
    print(-1)