import sys

num = int(sys.stdin.readline())
if num == 1:
    print("*")
else:
    for i in range(1, num, 1):
        j = num - i
        k = i*2 - 1
        print(" "*j+"*"*k)
    print("*"*(num*2-1))
    for i in range(num-1, 0, -1):
        j = num - i
        k = i*2 - 1
        print(" "*j+"*"*k)