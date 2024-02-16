N = int(input())
graph = [0] * N
for i in range(N):
    graph[i] = list(map(int, input().split()))
visited = [False] * N

result = 4000000

def TSP(start, now, cost, depth):  # 처음 번호, 현재 번호, 합, 갯수
    global result
    if depth == N and graph[now][start]:
        cost += graph[now][start]
        if result > cost:
            result = cost
        return
    if cost > result:
        return
    for i in range(N):
        if not visited[i] and graph[now][i] != 0:
            visited[i] = True
            TSP(start, i, cost+graph[now][i], depth+1)
            visited[i] = False 
for i in range(N):
    visited[i] = True
    TSP(i, i, 0, 1)
    visited[i] = False
print(result)
