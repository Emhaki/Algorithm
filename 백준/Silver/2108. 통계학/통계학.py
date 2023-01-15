import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
result = []
num = []
num_list = []
for _ in range(N):
    result.append(int(input()))
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# 산술평균
print(round(sum(result)/N))
# 중간값
print(sorted(result)[len(result)//2])
result = sorted(result)
cnt_result = Counter(result).most_common()
# 최빈값

if len(cnt_result) > 1 and cnt_result[0][1] == cnt_result[1][1]: # 최빈값 2개 이상
    print(cnt_result[1][0])
else:
    print(cnt_result[0][0])

# 범위
print(max(result) - min(result))