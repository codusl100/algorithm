N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]

def dfs(v):
    for i in range(N):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i) # 연결된게 있는지 확인 위해 dfs 돌림
visited = [0 for _ in range(N)]

for i in range(N):
    dfs(i) # 한 행마다 dfs 돌림
    for j in range(N):
        if visited[j] == 1:
            print(1, end = ' ')
        else :
            print(0, end = ' ')
    print()
    visited = [0 for _ in range(N)]