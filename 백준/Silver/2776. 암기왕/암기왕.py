import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    list_1 = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    list_2 = list(map(int, sys.stdin.readline().split()))
    for n in list_2:
        print(1 if n in list_1 else 0)