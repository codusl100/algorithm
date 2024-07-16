N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
def recur():
    if len(ans) == M:
        print(*ans)
        return
    for i in arr:
        if i not in ans:
            ans.append(i)
            recur()
            ans.pop()
recur()