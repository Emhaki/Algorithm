a, b, c = map(int, input().split())

list_ = []
list_.append(a)
list_.append(b)
list_.append(c)
result = sorted(list_)
print(*result)