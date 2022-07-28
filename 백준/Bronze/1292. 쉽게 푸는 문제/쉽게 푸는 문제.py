a, b = map(int, input().split())

num_list = [0]
for i in range(46):
    for j in range(i):
        num_list.append(i)

print(sum(num_list[a:b+1]))