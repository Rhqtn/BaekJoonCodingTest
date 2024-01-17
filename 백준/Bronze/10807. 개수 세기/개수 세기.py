import sys

amount = int(sys.stdin.readline())
numbers = sys.stdin.readline()
l = list(map(int, numbers.split(" ")))
s = int(sys.stdin.readline())
count = 0
for i in l:
    if i == s:
        count += 1
print(count)
