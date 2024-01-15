import sys

inputCount = int(sys.stdin.readline())
for i in range(inputCount):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)