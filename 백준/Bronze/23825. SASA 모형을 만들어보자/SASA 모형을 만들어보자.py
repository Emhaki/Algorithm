N, M = map(int, input().split())

# N과 M이 2개, 2개 일때마다 SASA모형 완성
temp = min(N, M)

print(temp//2)