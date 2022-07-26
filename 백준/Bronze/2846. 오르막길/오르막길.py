T = int(input())
a_list = list(map(int, (input().split())))
a = 0
b_list = []

# a_list = [1, 2, 1, 4, 6]
for i in range(T-1):
    if a_list[i] < a_list[i+1]:
        a += a_list[i+1] - a_list[i]
    else:
        b_list.append(a)
        a = 0

b_list.append(a)
print(max(b_list))