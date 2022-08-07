N, M = map(int, input().split())
dic_ = {}

for _ in range(N):
    name = input()
    dic_[name] = name
list_ = []
for _ in range(M):
    name2 = input()
    if name2 in dic_:
        list_.append(name2)
print(len(list_))
for i in sorted(list_):
    print(i)