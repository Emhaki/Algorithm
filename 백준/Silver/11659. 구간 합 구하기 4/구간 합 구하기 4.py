import sys
input = sys.stdin.readline

# N 수의 개수
# M 구해야하는 합 횟수 M
N, M = map(int, input().split())

num_list = list(map(int, input().split()))
sum_list = [0]
result = 0

for i in range(len(num_list)):
    result += num_list[i] # 구간의 합을 result에 저장
    sum_list.append(result) # 구간의 합을 sum_list에 append

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i - 1])