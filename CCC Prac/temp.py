n = int(input())
ans = []
for i in range(n * 2):
    ans.append(input())
newlist = [i for i, j in zip(ans[0:n], ans[n::]) if i == j]
print(len(newlist))
