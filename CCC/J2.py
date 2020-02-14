p = int(input())
n = int(input())
r = int(input())
total = 0
days = 0
total = n
totall = 0
while True:
    totall += total
    total *= r
    if totall <= p:
        days += 1
    else:
        break
print(days)