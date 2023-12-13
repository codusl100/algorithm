from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split()) # 시험관 크기, 바이러스 최대
S, X, Y = map(int, input().split())

graph = []
data = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        # 바이러스 있으면
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()

def bfs(data):
    queue = deque(data)
    while queue:
        virus, s, x, y = queue.popleft()
        if s == S: # s초가 지나거나 큐가 빌 때까지 반복
            break 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if graph[nx][ny] == 0: # 감염 전
                    graph[nx][ny] = virus
                    queue.append((virus, s+1, nx, ny))
           
bfs(data)
print(graph[X-1][Y-1])