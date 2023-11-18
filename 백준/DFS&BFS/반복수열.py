A, P = map(int, input().split()) # 57, 2
visited = [0]*250000 # 최댓값 4*9^5
count = 1

def square(a, p):
    ans = 0
    for i in str(a):
        ans += pow(int(i), p)
    return ans

def dfs(v, p, count, visited):
    if visited[v] != 0:
        return visited[v] -1
    visited[v] = count
    next = square(v, p)
    count += 1

    return dfs(next, p, count, visited)


print(dfs(A, P, count, visited))