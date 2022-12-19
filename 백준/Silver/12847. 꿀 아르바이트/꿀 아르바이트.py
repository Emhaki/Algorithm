a, b = map(int, input().split())
list_ = list(map(int, input().split()))

result_sum = [0]*(a+1)
for i in range(1, a+1):
  result_sum[i] = result_sum[i-1] + list_[i-1]

result = []
for i in range(b, a):
  result.append(result_sum[i] - result_sum[i-b])
print(max(result))