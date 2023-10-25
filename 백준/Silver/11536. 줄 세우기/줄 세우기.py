import sys
input = sys.stdin.readline

N = int(input().rstrip())
list_ = []
for _ in range(N):
    list_.append(str(input().strip()))
dic_list = sorted(list_)
answer = "NEITHER"
if list_ == dic_list:
    answer = "INCREASING"
elif list_ == dic_list[::-1]:
    answer = "DECREASING"
print(answer)