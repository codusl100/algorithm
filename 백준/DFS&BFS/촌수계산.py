from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q1, q2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited = [0] * (N+1)

def bfs(graph, start, visited):
	queue = deque([start])
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if visited[i] == 0:
				visited[i] = visited[v] + 1
				queue.append(i)
				
bfs(graph, q1, visited)
print(visited[q2] if visited[q2] > 0 else -1)