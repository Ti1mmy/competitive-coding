shift = int(input())
alphabet = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

sheldon = input()
leonard = []
for i in range(len(sheldon)):
    leonard.append(alphabet[(alphabet.index(sheldon[i]) - 3*(i+1) - shift)])
print("".join(leonard))
