class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visit = [False for _ in range(n)]
        
        for list in connections:
            a, b = list[0], list[1]
            graph[a].append(b)
            graph[b].append(-a)
        
        def dfs(v):
            visit[v] = True
            ans = 0
            
            for n in graph[v]:
                if visit[abs(n)] == False:
                    if n >= 0:
                        ans += 1
                    ans += dfs(abs(n))
            return ans
        return dfs(0)