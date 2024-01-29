import sys

word = sys.stdin.readline()
x = []
for i in range(97,123):
    state = 0
    for j in range(len(word)):
        if word[j] == chr(i):
            state = j
            break;
        else:
            state = -1
    x.append(state)
print(*x)