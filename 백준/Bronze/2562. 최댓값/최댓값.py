list_ = []
for i in range(9):
    list_.append(int(input()))

print(max(list_))
print(list_.index(max(list_))+1)