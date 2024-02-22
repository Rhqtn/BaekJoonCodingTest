import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
if a == 1:
    a = 0
elif a < 1:
    a = 1
else:
    count = 0
    while a != 1:
        a -= 1
        count -= 1
    a = count
#/***************************/
if b == 1:
    b = 0
elif b < 1:
    b = 1
else:
    count = 0
    while b != 1:
        b -= 1
        count -= 1
    b = count
    #/***************************/
if c == 2:
    c = 0
elif c < 2:
    count = 0
    while c != 2:
        c += 1
        count += 1
    c = count
else:
    count = 0
    while c != 2:
        c -= 1
        count -= 1
    c = count
    #/***************************/
if d == 2:
    d = 0
elif d < 2:
    count = 0
    while d != 2:
        d += 1
        count += 1
    d = count
else:
    count = 0
    while d != 2:
        d -= 1
        count -= 1
    d = count
    #/***************************/
if e == 2:
    e = 0
elif e < 2:
    count = 0
    while e != 2:
        e += 1
        count += 1
    e = count
else:
    count = 0
    while e != 2:
        e -= 1
        count -= 1
    e = count
    #/***************************/

if f == 8:
    f = 0
elif f < 8:
    count = 0
    while f != 8:
        f += 1
        count += 1
    f = count
else:
    count = 0
    while f != 8:
        f -= 1
        count -= 1
    f = count

print(a,b,c,d,e,f)