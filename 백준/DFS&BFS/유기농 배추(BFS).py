# 재귀 limit 설정
from collections import deque
import sys
sys.setrecursionlimit(10000)

T = int(input())
worm = 0
result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(farm, a, b):
    global result
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and farm[nx][ny] == 1: # 방문 안했으면
                farm[nx][ny] = 0
                queue.append((nx, ny))
    return 1

for i in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 개수
    farm = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        farm[a][b] = 1 
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:
                result += bfs(farm, i, j)
                

    print(result)
    result = 0
