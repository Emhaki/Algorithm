import sys
input = sys.stdin.readline

from itertools import combinations

while True:
    s = input().strip().split(" ")[1:]
    if s == []:
        break
    for i in combinations(s, 6):
        print(*i)
    print(" ")