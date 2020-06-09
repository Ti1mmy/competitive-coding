from sys import stdin, stdout
a = int(stdin.readline())
b = stdin.readline().split(" ")
b = [int(i) for i in b]
b.sort()
low = []
high = []
output = []
for i in range(a):
    if i % 2==0:
        low.append(b.pop(0))
    else:
        high.append(b.pop(-1))
while high or low:
    if low:
        output.append(low.pop(-1))
    if high:
        output.append(high.pop(-1))
output = [str(i) for i in output]
stdout.write(" ".join(output))
