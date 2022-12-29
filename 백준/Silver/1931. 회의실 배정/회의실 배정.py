N = int(input())
list_ = []
for i in range(N):
  a,b = map(int, input().split())
  list_.append([a,b])

list_ = sorted(list_, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
list_ = sorted(list_, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
last = 0
count = 0
for i, j in list_:
  if i >= last:
    count += 1
    last = j # 여기가 핵심 (마지막 시간을 계속해서 저장)
print(count)