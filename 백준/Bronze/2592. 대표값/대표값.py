num_dic = {}
num_sum = 0
for _ in range(10):
    number = int(input())
    num_sum += number
    if number not in num_dic:
        num_dic[number] = 1
    else:
        num_dic[number] += 1

print(num_sum//10)
# num_dic = {10: 1, 40: 2, 30: 3, 60: 2, 20: 1, 50: 1}
many_num = max(num_dic.values())
for k, v in num_dic.items():
    if v == many_num:
        print(k)