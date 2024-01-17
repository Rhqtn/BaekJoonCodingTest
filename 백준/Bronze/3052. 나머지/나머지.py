import sys
baskets = []
count = 0
for i in range(10):
    temp = int(sys.stdin.readline())%42
    if temp in baskets:
        continue
    else:
        count += 1
    baskets.append(temp)
    
print(count)