x = input()
dic_ = {}
list_ = list(map(int, input().split()))
num = int(input())

for i in list_:
    if i not in dic_:
        dic_[i] = 1
    else:
        dic_[i] += 1

if num in dic_:
    for k, v in dic_.items():
        if k == num:
            print(v)
else:
    print(0)