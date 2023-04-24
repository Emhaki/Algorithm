import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = 0

def dfs(arr, total):
    global answer
    if len(arr) == 2:
        answer = max(answer, total)
        return 
    
    for i in range(1, len(arr)-1):
        dfs(arr[:i] + arr[i+1:], total + (arr[i-1] * arr[i+1]))

dfs(arr, answer)
print(answer)