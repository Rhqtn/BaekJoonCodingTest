import sys

amount, x = map(int, sys.stdin.readline().split())
numbers = sys.stdin.readline()
l = list(map(int, numbers.split(" ")))
smallerList = []
for i in l:
    if i < x:
        smallerList.append(i)
print(*smallerList)
