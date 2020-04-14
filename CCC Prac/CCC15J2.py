a = input().split()
happ = 0
sad = 0
for str in a:
    happ += str.count(':-)')
    sad += str.count(':-(')
if not happ and not sad:
    print('none')
elif happ == sad:
    print('unsure')
elif happ > sad:
    print('happy')
else:
    print('sad')
