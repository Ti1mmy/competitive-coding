t = input()
s = input()
shifts = []
x = []
yes = False
for i in range(len(s)):
    x.append(s[i])
for i in range(len(s)):
    temp = s[i:] + s[:i]
    shifts.append(temp)
for shift in shifts:
    if shift in t:
        yes = True
        break
if yes:
    print('yes')
else:
    print('no')