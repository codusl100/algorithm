N, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
distance = [i for i in range(D + 1)]

for i in range(D + 1):
    # 지름길로 간 거리와 고속도로로 간 거리 비교
    distance[i] = min(distance[i], distance[i-1] + 1)

    # 지름길을 반복하여 최단 경로 찾음
    for start, end, short in graph:
        if i == start and end <= D and distance[i] + short < distance[end]:
            distance[end] = distance[i] + short

print(distance[D])