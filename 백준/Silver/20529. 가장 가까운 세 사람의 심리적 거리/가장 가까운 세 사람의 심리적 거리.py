from itertools import combinations
import sys
input = sys.stdin.readline

def mbti_dist(a, b):
    distance = 0
    for i, j in zip(a, b):
        if i != j:
            distance += 1
    return distance

T = int(input().strip())
for _ in range(T):
    N = int(input())
    mbti = input().strip().split()

    if N > 32:
        print(0)
    else:
        result = 13
        case = combinations(mbti, 3)
        for a, b, c in case:
            distance = 0
            distance += mbti_dist(a, b)
            distance += mbti_dist(b, c)
            distance += mbti_dist(a, c)

            result = min(result, distance)
        print(result)