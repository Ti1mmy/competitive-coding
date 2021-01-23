n = int(input())
k = int(input())
l = n
for i in range(k):
    n *= 10
    l += n
print(l)
