num_list = []
for _ in range(5):
    number = int(input())
    num_list.append(number)

print(sum(num_list)//5)
print(sorted(num_list)[2])