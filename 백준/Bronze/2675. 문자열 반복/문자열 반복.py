import sys

count = int(sys.stdin.readline())

for i in range(count):
    x, word = map(str, sys.stdin.readline().rstrip().split(" "))
    x = int(x)
    wordList = []
    for j in range(len(word)):
        wordList.append(x*word[j])
    print(*["".join(wordList)])
