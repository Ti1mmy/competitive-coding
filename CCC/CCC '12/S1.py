from math import factorial
scorer = int(input())
try:
    print((factorial(scorer-1)//(factorial(4) * (factorial(scorer - 4)))) * 4)
except ValueError:
    print(0)