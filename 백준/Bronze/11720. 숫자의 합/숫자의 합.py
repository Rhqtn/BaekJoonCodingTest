import sys

amount = int(sys.stdin.readline())
x = sys.stdin.readline()
sum = 0
for i in range(amount):
    sum += int(x[i])
print(sum)