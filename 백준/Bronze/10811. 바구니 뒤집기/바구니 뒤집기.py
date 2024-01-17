import sys

bNumber, amount = map(int, sys.stdin.readline().split())
baskets = []
for i in range(bNumber):
    baskets.append(i+1)

for i in range(amount):
    i, j = map(int, sys.stdin.readline().split())
    tempBaskets = baskets[i-1:j]
    tempBaskets.reverse()
    baskets[i-1:j] = tempBaskets
print(*baskets)