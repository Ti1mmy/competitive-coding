mass = []
masssum = [0]
tmass = []
for i in range(int(input())):
    mass.append(int(input()))
for i in range(len(mass)):
    masssum.append(masssum[i] + mass[i])
for i in range(int(input())):
    a = input()
    a.split()
    print(a)
    tmass.append(masssum[int(a[2])] - masssum[(a[0])])
for i in range(len(tmass)):
    print(tmass[i])
