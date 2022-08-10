N = int(input())

cow_dic = {}
cross = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a not in cow_dic:
        cow_dic[a] = b
    elif a in cow_dic and b != cow_dic[a]:
        cow_dic[a] = b
        cross += 1

print(cross)