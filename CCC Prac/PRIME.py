n = int(input())
def factors(n):
    f = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            f += 1
    return f
if n == 1:
    print(2)
elif n <= 3 or n == 5:
    print(n)
else:
    f = factors(n)
    while f != 1:
        n += 1
        f = factors(n)
    print(n)





