import sys
input = sys.stdin.readline
N, M = map(int, input().split())

INF = int(1e9)
graph = []
distance = [INF] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost
                if i == N - 1:
                    return True
    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])