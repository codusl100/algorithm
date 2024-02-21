from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dfs_list = [V]
bfs_list = [V]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0: # 방문 안했으면
            dfs_list.append(i)
            dfs(i)
def bfs(graph, V, visited):
    queue = deque([V])
    visited[V] = 1
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i] == 0: # 방문 안했으면
                visited[i] = 1
                bfs_list.append(i)
                queue.append(i)
dfs(V) 
visited = [0] * (N+1)
bfs(graph, V, visited)

print(' '.join(str(item) for item in dfs_list))
print(' '.join(str(item) for item in bfs_list))


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs_list.append(i)
            dfs(i)

def bfs(graph, V, visited):
    queue = deque([V])
    visited[V] = 1
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited[i] == 0:
                visited[i] = 1
                bfs_list.append(i)
                q.append(i)