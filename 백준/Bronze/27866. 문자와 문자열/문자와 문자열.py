import sys

word = sys.stdin.readline()
spWord = [*word]
number = int(sys.stdin.readline())
print(spWord[number-1])