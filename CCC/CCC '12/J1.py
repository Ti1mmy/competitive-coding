s1 = int(input())
s2 = int(input())
s3 = 0
if s2 - s1 < 2:
    print('Congratulations, you are within the speed limit!')
elif s2 - s1 < 21:
    s3 = 100
elif s2 - s1 < 31:
    s3 = 270
else:
    s3 = 500
if s3 != 0:
    print(f'You are speeding and your fine is ${s3}.')