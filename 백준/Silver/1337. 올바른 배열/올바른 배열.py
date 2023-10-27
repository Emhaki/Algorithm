import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = []
answer = 5
for i in range(N):
    nums.append(int(input()))

for i in range(N):
    cnt1 = 4
    cnt2 = 4
    for j in range(N):
        if nums[i] + 5 > nums[j] and nums[i] < nums[j]:
            cnt1 -= 1
        elif nums[i] - 5 < nums[j] and nums[i] > nums[j]:
            cnt2 -= 1
    answer = min(answer, cnt1, cnt2)
print(answer)