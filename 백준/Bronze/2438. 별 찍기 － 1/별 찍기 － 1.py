import sys

starCount = int(sys.stdin.readline())
star = "*"
for i in range(starCount):
   print((star*(i+1)).lstrip())