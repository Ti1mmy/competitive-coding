import sys
input = sys.stdin.readline
k = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0
]
i = 0
noun = 0
verb = 0
increment = False
while True:
    if increment:
        noun += 1
        verb = 0
        increment = False
    else:
        verb += 1
    if verb == 99:
        increment = True
    k[1] = noun
    k[2] = verb
    while True:
        if k[i] == 1:
            b = k[k[i + 1]] + k[k[i + 2]]
        elif k[i] == 2:
            b = k[k[i + 1]] * k[k[i + 2]]
        else:
            break
        k[k[i + 3]] = b
        i += 4
    print(k[0])
    print(noun, verb)
    if k[0] == 19690720:
        break
    elif noun == 99 and verb == 99:
        break
    else:
        k = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 9, 19, 1, 10, 19, 23, 2, 9, 23, 27, 1, 6, 27, 31, 2,
             31, 9, 35, 1, 5, 35, 39, 1, 10, 39, 43, 1, 10, 43, 47, 2, 13, 47, 51, 1, 10, 51, 55, 2, 55, 10, 59, 1, 9,
             59, 63, 2, 6, 63, 67, 1, 5, 67, 71, 1, 71, 5, 75, 1, 5, 75, 79, 2, 79, 13, 83, 1, 83, 5, 87, 2, 6, 87, 91,
             1, 5, 91, 95, 1, 95, 9, 99, 1, 99, 6, 103, 1, 103, 13, 107, 1, 107, 5, 111, 2, 111, 13, 115, 1, 115, 6,
             119, 1, 6, 119, 123, 2, 123, 13, 127, 1, 10, 127, 131, 1, 131, 2, 135, 1, 135, 5, 0, 99, 2, 14, 0, 0
             ]
        i = 0