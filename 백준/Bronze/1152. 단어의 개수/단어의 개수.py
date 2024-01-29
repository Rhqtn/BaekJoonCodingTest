import sys

sent = list(map(str, sys.stdin.readline().rstrip().lstrip().split(" ")))
if len(sent[0]) == 0:
    print(0)
else:
    print(len(sent))