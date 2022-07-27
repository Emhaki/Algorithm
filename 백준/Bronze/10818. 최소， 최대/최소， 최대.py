N = int(input())
# input 값을 각각의 리스트에 넘는 수식
nums = list(map(int, input().split()))

print(min(nums), max(nums))