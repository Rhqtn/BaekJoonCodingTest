import sys

a, b = map(str, sys.stdin.readline().rstrip().split(" "))
newA = []
newB = []
for i in range(-1, -4, -1):
    newA.append(a[i])
newA = int("".join(newA))

for i in range(-1, -4, -1):
    newB.append(b[i])
newB = int("".join(newB))

if newA <= newB:
    print(newB)
else:
    print(newA)
