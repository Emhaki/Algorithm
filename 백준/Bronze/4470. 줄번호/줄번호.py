list_ = []
for _ in range(int(input())):
    list_.append(input())
for i in list_:
    print(f'{list_.index(i)+1}. {i}')