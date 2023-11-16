import sys
input = sys.stdin.readline
R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]
visited = [0] * 26
visited[ord(graph[0][0])-65] = 1
max_ = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    global max_
    max_ = max(max_, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < R) and (0 <= ny < C):
            if visited[ord(graph[nx][ny]) - 65] == 0:
                visited[ord(graph[nx][ny]) - 65] = 1
                dfs(nx, ny, cnt+1)
                visited[ord(graph[nx][ny]) - 65] = 0


dfs(0, 0, max_)

print(max_)