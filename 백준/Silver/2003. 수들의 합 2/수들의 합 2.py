import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# 구간 초기화
start, end = 0, 1

# m이 되는 경우의 수
cnt = 0

while (start <= end and end <= N):
    
    # 구간의 합 계산
    total = sum(num_list[start:end])

    # 구간의 합이 목표값보다 작으면
    if (total < M):
        # end idx를 오른쪽으로 이동
        end += 1
    
    elif (total > M):
        # start idx를 오른쪽으로 한 칸 이동
        start += 1
    
    elif total == M:
        # 경우의 수 증가
        cnt += 1
        # 끝 idx를 오른쪽으로 한 칸 이동
        end += 1

print(cnt)