import sys
baskets = []
for i in range(30):
    baskets.append(i+1)
for i in range(28):
    temp = int(sys.stdin.readline())
    baskets[temp-1] = 31
baskets.sort()
print(baskets[0])
print(baskets[1])