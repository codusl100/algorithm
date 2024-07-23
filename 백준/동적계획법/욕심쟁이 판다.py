import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input()) # 그래프의 크기

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(n)] for _ in range(n)]

def recur(y, x):
	point = 1
	for dy, dx in [[0,1],[0,-1],[1,0],[-1,0]]:
		ey = y + dy
		ex = x + dx
		
		if 0 <= ey < n and 0 <= ex < n:
			if graph[y][x] < graph[ey][ex]:
				if dp[ey][ex] != -1: # 방문했던 곳이라면
					point = max(point, dp[ey][ex] + 1)
				else:
					point = max(point, recur(ey, ex) + 1)
	dp[y][x] = point
	return dp[y][x]

result = 0
for y in range(n):
	for x in range(n):
		result = max(result, recur(y,x))
		
print(result)