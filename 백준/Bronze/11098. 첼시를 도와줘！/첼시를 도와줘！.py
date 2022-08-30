n = int(input())
for _ in range(n):
    dic_ = {}
    list_ = []
    p = int(input())
    for _ in range(p):
        v, k = input().split()
        dic_[v] = k
        list_.append(int(v))
    print(dic_[str(max(list_))])