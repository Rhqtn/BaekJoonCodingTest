totalAmount = int(input())
numberCount = int(input())
totalSum = 0
for i in range(numberCount):
  price, amount = map(int, input().split())
  totalSum += price*amount
if totalAmount == totalSum:
  print("Yes")
else:
  print("No")