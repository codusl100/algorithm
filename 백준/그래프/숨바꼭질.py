from collections import deque
N, K = map(int, input().split()) # 수빈이가 있는 위치, 동생이 있는 위치
visited = [0] * 200001

def bfs(v):
    q = deque([(v)])
    visited[v] = 1
    while q:
        curr = q.popleft()
        if curr == K :
            return
        for nn in (curr + 1, curr - 1, curr * 2):
            if 0<=nn<=100000:
                if visited[nn] == 0 or visited[curr] + 1 < visited[nn]:
                    visited[nn] = visited[curr] + 1
                    q.append(nn)   
bfs(N)
print(visited[K] - 1)        