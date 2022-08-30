dic_ = {}
list_ = []
for _ in range(int(input())):
    name, d, m, y = input().split()
    age = int(y)+int(m)*1/12+int(d)*1/360
    list_.append(age)
    dic_[age] = name
print(dic_[max(list_)])
print(dic_[min(list_)])