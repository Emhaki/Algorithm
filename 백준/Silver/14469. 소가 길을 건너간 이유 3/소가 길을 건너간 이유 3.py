N = int(input())
list_ = []
time = 0

for i in range(N):
    a, b = map(int, input().split(" "))
    list_.append((a, b))

list_.sort()

for i in range(len(list_)):
    if time > list_[i][0]: # 다음 소 이전 소가 검문 받고 있는 중에 도착했을 때
        time = time + list_[i][1]
    else:
        time = list_[i][0] + list_[i][1]

print(time)