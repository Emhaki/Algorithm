import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coin = [list(map(int, input().strip())) for _ in range(N)]
cnt = 0

def rev(x, y):
    
    for i in range(x+1):
        for j in range(y+1):
            # i,j 가 1이라면 0으로 만듬
            if coin[i][j] == 1:
                coin[i][j] = 0
            # 아니라면 1로 만듬
            else:
                coin[i][j] = 1

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1): # 가장 오른쪽 아래부터
        if coin[i][j]:
            cnt += 1 # 뒤집는 횟수 카운트

            rev(i,j)

print(cnt)