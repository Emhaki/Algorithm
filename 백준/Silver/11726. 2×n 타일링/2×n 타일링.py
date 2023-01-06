n = int(input())
list_ = [0] * 1001

list_[1]= 1
list_[2]= 2

for i in range(3, 1001):
  list_[i] = (list_[i-1]+list_[i-2])%10007

print(list_[n])