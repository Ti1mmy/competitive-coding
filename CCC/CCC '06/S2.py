known = [char for char in input()]
cipher = [char for char in input()]
decrypt = [char for char in input()]

dictionary = dict(zip(cipher, known))

cracked = []
for char in decrypt:
    try:
        cracked.append(dictionary[char])
    except KeyError:
        cracked.append(".")
print("".join(cracked))
