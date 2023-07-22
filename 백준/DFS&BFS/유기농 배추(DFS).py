# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

T = int(input())
worm = 0
result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if farm[x][y] == 1: 
        farm[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny) 
        return True
    return False

for i in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        farm[a][b] = 1
    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                result += 1

    print(result)
    result = 0