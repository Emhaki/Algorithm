A, X = map(int, input().split())
# input 값을 각각의 리스트에 넘는 수식
nums = list(map(int, input().split()))

for num in nums:
    if num < X:
        print(num, end=" ")