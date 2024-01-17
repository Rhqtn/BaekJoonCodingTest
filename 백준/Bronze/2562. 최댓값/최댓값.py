import sys

lst = 0
count = 0
for i in range(9):
    newNum = int(sys.stdin.readline())
    if newNum > lst:
        lst = newNum
        count = i+1
print(lst)
print(count)
