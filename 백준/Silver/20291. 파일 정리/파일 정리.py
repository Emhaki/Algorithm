import sys

N = int(sys.stdin.readline())
dic_ = {}
for _ in range(N):
    v, k = map(str, sys.stdin.readline().strip().split('.'))
    if k not in dic_:
        dic_[k] = 1
    else:
        dic_[k] += 1
for i in (sorted(dic_.items())):
    print(*i)