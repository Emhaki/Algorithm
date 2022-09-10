T = int(input())
dic_ = {}
max_num = 0
for _ in range(T):
    N = int(input())
    for _ in range(N):
        a, b = input().split()
        dic_[a] = int(b)
        if max_num < int(b):
            max_num = int(b)
    for k, v in dic_.items():
        if v == max_num:
            print(k)