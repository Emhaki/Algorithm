N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

for i in sorted(num_list):
    print(i)