from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, P = map(int, input().split()) 

# index는 싫어하는 채널, 그 안에 값들은 싫어하는 사람들
visited = [0] * (M+1)
fav = {}
cnt = 0

for i in range(N):
    f, d = map(int, input().split())
    if fav.get(d) == None: # 싫어하는 채널 해당 안되는 경우
        fav[d] = f

def dfs(v): 
    global cnt 
    if visited[v] == 0: # 채널 안바꿨으면
        visited[v] = 1 # 방문
        if fav.get(v) != None :
            cnt += 1
            dfs(fav.get(v))
    elif visited[v] == 1:
        cnt = -1
    return cnt
 # P는 채널
print(dfs(P)) 