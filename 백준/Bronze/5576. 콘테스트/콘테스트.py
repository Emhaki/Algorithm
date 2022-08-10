A_group = []
B_group = []
for _ in range(10):
    A_group.append(int(input()))
for _ in range(10):
    B_group.append(int(input()))
A_group = sorted(A_group, reverse=True)
B_group = sorted(B_group, reverse=True)
A_group_sum = 0
B_group_sum = 0

for i in range(3):
    A_group_sum += A_group[i]
for j in range(3):
    B_group_sum += B_group[j]
print(A_group_sum, B_group_sum)