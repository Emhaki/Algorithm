T = int(input())

for _ in range(T):
    list_ = list(map(int, input().split()))
    list_ = sorted(list_)
    list_ = list_[::-1]
    print(list_[2])