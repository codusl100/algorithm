def solution(n, computers):
    visited = [0 for i in range(n)]
    result = 0
    def dfs(v):
        visited[v] = 1
        for x in range(n):
            if x != v and computers[v][x] == 1: # 연결된 컴퓨터라면
                if visited[x] == 0:
                    dfs(x)

    for i in range(n):
        if visited[i] == 0 :
            dfs(i)  
            result += 1
    print(result)

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])