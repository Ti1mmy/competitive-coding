a = input()
if len(a) == 1:
    print(a)
else:
    thing = []
    for i in range(len(a)):
        thing.append(a[i:] + a[:i])
        thing.append((a[i:] + a[:i])[::-1])
    thing.sort()
    for t in thing:
        print(t)