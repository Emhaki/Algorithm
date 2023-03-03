import sys
input = sys.stdin.readline

N, X = map(int, input().split())

burger = [1] * 51 # 버거 레이아웃
patty = [1] * 51 # 버거의 패티 갯수

for i in range(1, N+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
    patty[i] = patty[i-1] + 1 + patty[i-1]

def hamburger(n, x):
    if n == 0:
        return x
    if x == 1:
        return 0
    elif x <= 1 + burger[n-1]:
        return hamburger(n-1, x-1)
    elif x == 1 + burger[n-1] + 1:
        return patty[n-1] + 1
    elif x <= burger[n-1] + burger[n-1] + 1 + 1:
        return patty[n-1] + 1 + hamburger(n-1, (x-(burger[n-1]+2)))
    else:
        return patty[n]

print(hamburger(N, X))
