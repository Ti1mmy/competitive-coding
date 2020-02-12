import sys
input = sys.stdin.readline
games = int(input()[:-1])
track = input()[:-1].split()
track_int = [int(score) for score in track]
opp = input()[:-1].split()
opp_int = [int(score) for score in opp]
win = 0
for i in range(games):
    if track_int[i] > opp_int[i]:
        win += 1
    elif track_int[i] < opp_int[i]:
        win -= 1
print(win)