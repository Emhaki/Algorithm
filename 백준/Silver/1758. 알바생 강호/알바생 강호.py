N = int(input())
list_ = []
for i in range(N):
    list_.append(int(input()))

# 돈 - (받은 등수 - 1)
list_.sort(reverse=True)
result = 0

for i in range(len(list_)):
    if list_[i] - ((i+1) - 1) >= 0:
        result += list_[i] - ((i+1) - 1)

print(result)