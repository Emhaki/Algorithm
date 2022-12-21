from itertools import combinations

N = int(input())
result = [0]*N
for i in range(N):
  number = 0
  num_list = list(map(int, input().split()))
  num = list(combinations(num_list, 3))
  for j in num:
    if sum(j) % 10 > number:
      number = sum(j) % 10
      result[i] = number

for i in range(N - 1, -1, -1): # 두 명 이상일 경우 번호가 가장 큰 사람의 번호를 구하기 위해
  if result[i] == max(result):  # 제일 높은 점수 찾기
    print(i + 1)
    break