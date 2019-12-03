i = input()
k = i.split(",")
for i in range(len(k)):
    k[i] = int(k[i])
i = 0
while True:
    if k[i] == 1:
        b = k[k[i + 1]] + k[k[i + 2]]
    elif k[i] == 2:
        b = k[k[i + 1]] * k[k[i + 2]]
    else:
        break
    k[k[i + 3]] = b
    i += 4
print(k)