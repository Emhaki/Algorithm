import sys
input = sys.stdin.readline
# P는 올라갈 수 있는 랭킹의 수
# 0 <= N <= P
N, score, P = map(int, input().split())
grade = list(map(int, input().split()))

if N == 0:
    print(1)
else:
    if N == P and grade[-1] >= score:
        print(-1)
    else:
        result = N + 1
        for i in range(N):
            if grade[i] <= score:
                result = i + 1
                break
        print(result)