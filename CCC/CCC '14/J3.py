ant = 100
dav = 100
for i in range(int(input())):
    rolls = input().split(" ")
    rolls = [int(roll) for roll in rolls]
    if rolls[0] < rolls[1]:
        ant -= rolls[1]
    elif rolls[0] > rolls[1]:
        dav -= rolls[0]
print(ant)
print(dav)