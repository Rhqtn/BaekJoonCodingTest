h, m = map(int, input().split())
cookTime = int(input())

h = (h + (m + cookTime) // 60) % 24
m = (m + cookTime) % 60
print(f"{h} {m}")
