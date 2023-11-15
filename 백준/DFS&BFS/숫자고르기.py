N = int(input())
result = 0
graph = [[] for _ in range(N + 1)]
ans = []
for i in range(1, N+1):
    graph[i].append(int(input()))

print(graph)

def dfs(v):
    if visited[v]== 0:
        visited[v] = 1
        for i in graph[v]:
            tmp_up.add(v)
            tmp_bottom.add(i) 
            if tmp_bottom == tmp_up:
                ans.extend(list(tmp_bottom))
                return
            dfs(i)
    visited[v] = 0

for i in range(1, N+1):
    visited = [0] * (N+1) 
    tmp_up = set()
    tmp_bottom = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans:
    print(a)