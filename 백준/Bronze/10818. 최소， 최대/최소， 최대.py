import sys

amount =int(sys.stdin.readline())
numbers = sys.stdin.readline()
l = list(map(int, numbers.split(" ")))
smallast = l[0]
largest = l[0]
for i in l:
    if i > largest:
        largest = i
    if i < smallast:
        smallast = i
print(smallast, largest)
