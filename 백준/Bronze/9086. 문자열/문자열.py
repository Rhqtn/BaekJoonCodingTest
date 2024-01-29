import sys

countNum = int(sys.stdin.readline())
for i in range(countNum):
    chr = sys.stdin.readline()
    print(chr[0]+chr[-2])