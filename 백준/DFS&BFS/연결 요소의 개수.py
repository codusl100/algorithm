import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
visited = [0] * (N+1)
result = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for x in graph[v]:
        if visited[x] == 0:
            dfs(x)

for i in range(1, N+1):
    if visited[i] == 0 :
        dfs(i)  
        result += 1

print(result)