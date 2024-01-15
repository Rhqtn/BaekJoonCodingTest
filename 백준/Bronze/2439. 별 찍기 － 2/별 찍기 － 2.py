import sys

starCount = int(sys.stdin.readline())
star = "*"
spaceCount = int(starCount) -1
for i in range(starCount):
   print(" "*spaceCount+(star*(i+1)).lstrip())
   spaceCount -= 1