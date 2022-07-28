count_list = []
result_list = []
for i in range(10):
    N = input()
    count_list.append(N)
for j in count_list:
    result_list.append(int(j) % 42)

result_set = set(result_list)
print(len(result_set))