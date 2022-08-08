list_ = []
for _ in range(9):
    list_.append(int(input()))
# list_ = [20, 7, 23, 19, 10, 15, 25, 8, 13]
for i in range(8):
    for j in range(i+1, 9):
        if sum(list_)-(list_[i]+list_[j]) == 100:  # i, j 가 순회하면서 100이랑 같아질 때
            x, y = i, j  # 그때의 인덱스 위치를 저장


for k in sorted(list_):  # 정렬된 리스트가
    if k != list_[x] and k != list_[y]:  # 해당값이 아닐때 출력
        print(k)