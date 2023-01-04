import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  rank = [list(map(int, input().split())) for _ in range(n)]
  rank = sorted(rank)
  top = 0
  result = 1

  for i in range(1, len(rank)):
    if rank[i][1] < rank[top][1]:
      top = i
      result += 1

  print(result)