from collections import deque
def solution(begin, target, words):
    n = len(words)
    visited = [0] * n
    ans = 0

    def bfs(v, visited, target, words):
        queue = deque([v])
        n = words.index(v)
        visited[n] = 1
        while queue:
            str = queue.popleft()
            if str == target:
                return
            if visited[n] == 0:
                visited[n] = 1
                queue.append(n+1)


    if target not in words:
        return 0
    else:
        bfs(words[0], visited, target, words)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


# def bfs(graph, V, visited):
#     queue = deque([V])
#     visited[V] = 1
#     while queue:
#         q = queue.popleft()
#         for i in graph[q]:
#             if visited[i] == 0: # 방문 안했으면
#                 visited[i] = 1
#                 bfs_list.append(i)
#                 queue.append(i)