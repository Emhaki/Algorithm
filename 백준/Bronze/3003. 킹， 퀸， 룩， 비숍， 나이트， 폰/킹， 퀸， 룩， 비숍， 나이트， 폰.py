chess_list = [1, 1, 2, 2, 2, 8]
input_list = list(map(int, input().split()))
result_list = []
for i in range(len(chess_list)):
    result_list.append((chess_list[i] - input_list[i]))

print(*result_list)