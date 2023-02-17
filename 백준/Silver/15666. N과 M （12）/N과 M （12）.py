import sys
input = sys.stdin.readline


n, m = map(int, input().split())
num_list = sorted(set(list(map(int, input().split()))))

result = []
answer = []

def solve(depth, idx):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(idx, len(num_list)):
        result.append(num_list[i])
        solve(depth+1, i)
        result.pop()

solve(0,0)
answer = sorted(list(set(answer)))