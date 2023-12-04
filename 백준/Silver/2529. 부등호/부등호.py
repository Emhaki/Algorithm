import sys
input = sys.stdin.readline

def get_num(x, y, operator):
    if operator == "<":
        if x > y:
            return False
    else:
        if x < y:
            return False
    return True

def dfs(idx, num):
    if idx == k+1:
        answer.append(num)
        return
    
    for i in range(10):
        if not check[i]:
            if idx == 0 or get_num(num[idx-1], str(i), operator[idx-1]):
                check[i] = True
                dfs(idx + 1, num + str(i))
                check[i] = False

k = int(input())
operator = list(input().split())

check = [False] * 10
answer = []
dfs(0, '')

answer.sort()
print(answer[-1])
print(answer[0])