N = int(input())
list_ = list(map(int, input().split()))
result_list = sorted(list_)
array = [0] * 10000

for i in range(N):
  array[i] = sum(result_list[:i+1])
print(sum(array))