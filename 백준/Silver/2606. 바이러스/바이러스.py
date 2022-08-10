n = int(input())  # 정점 개수(컴퓨터)
m = int(input())  # 간선 개수(네트워크)
graph = [[] for _ in range(n+1)]
total = 0

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    # 연결된 컴퓨터의 정보가 언제가 1부터 등장한다는 보장 x
    graph[v1].append(v2)
    graph[v2].append(v1)

# graph = [
# []
# [2,5],
# [1,3,5]
# [2],
# [7],
# [1,2,6]
# [5],
# [4]
# ]


def dfs(x, total):
    visited[x] = True
    for node in graph[x]:
        if not visited[node]:
            total = dfs(node, total + 1)
    return total


visited = [False for _ in range(n+1)]  # 방문 처리 리스트 만들기

print(dfs(1, 0))