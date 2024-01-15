a, b, c = map(int, input().split())
sameNumCount = 0
biggNum = a
if a == b:
  if b == c:
    sameNumCount = 3
  else:
    sameNumCount = 2
elif b == c:
  sameNumCount = 2
  biggNum = b
else:
  if a == c:
    sameNumCount = 2
  elif a < b :
    if b < c:
      biggNum = c
    else:
      biggNum = b
  elif a > c:
      biggNum = a
  else:
      biggNum = c
if sameNumCount == 0:
  print(f"{biggNum*100}")
elif sameNumCount == 2:
  print(f"{1000+biggNum*100}")
else:
  print(f"{biggNum*1000+10000}")

