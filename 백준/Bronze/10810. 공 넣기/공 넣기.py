import sys

bNumber, amount = map(int, sys.stdin.readline().split())
baskets = []
for i in range(bNumber):
    baskets.append(0)
for i in range(amount):
    i, j, k = map(int, sys.stdin.readline().split())
    for f in range(i-1,j):
        baskets[f] = k
print(*baskets)