nums = input().strip()
n = 0
index = 0
while True:
    n += 1
    for s in str(n):
        if nums[index] == s:
            index += 1
            if index >= len(nums):
                print(n)
                exit()