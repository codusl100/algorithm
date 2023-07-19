import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M, K = map(int, input().split()) # 세로, 가로, 음식물 쓰레기 개수

trash = [[0 for _ in range(M+1)] for i in range(N + 1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
result = []

for _ in range(K):
    a, b = map(int, input().split())
    trash[a][b] = 1

def dfs(x, y):
    global cnt
    if x <= 0 or x > N or y <= 0 or y > M:
        return False
    if trash[x][y] == 1:
        trash[x][y] = 0
        cnt += 1 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]       
            dfs(nx, ny) 
        return True
   
for i in range(N+1):
    for j in range(M+1):
        if dfs(i, j) == True:
            result.append(cnt)
            cnt = 0

print(max(result))