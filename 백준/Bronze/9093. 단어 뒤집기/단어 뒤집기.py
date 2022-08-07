T = int(input())
list2 = []
for _ in range(T):
    list_ = list(map(str, input().split()))

    for i in list_:  # ['I', 'am', 'happy', 'today']
        j = i[::-1]  # i를 각각 좌우반전
        list2.append(j)  # 반전시킨 j를 list2에 append
        list_ = list2  # 리스트를 삭제하기 위해 처음 받았던 list_에 할당
    print(*list_)
    list_.clear()