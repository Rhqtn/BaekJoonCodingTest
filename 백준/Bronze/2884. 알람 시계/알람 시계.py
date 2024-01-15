h, m = map(int, input().split())
if (m - 45) < 0:
    if h == 0:
      h = 23
    else:
      h -= 1
    m = m + 15
    print(f"{h} {m}")
else:
    print(f"{h} {m-45}")