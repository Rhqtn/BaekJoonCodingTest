import sys

amount = int(sys.stdin.readline())
l = sys.stdin.readline()
lst = list(map(int, l.split(" ")))
lst.sort()
sum = 0
for i in range(amount):
    sum += lst[i]/lst[-1]*100
print((sum)/amount)