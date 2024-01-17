import sys

bNumber, amount = map(int, sys.stdin.readline().split())
baskets = []
for i in range(bNumber):
    baskets.append(i+1)
for i in range(amount):
    i, j = map(int, sys.stdin.readline().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp
print(*baskets)