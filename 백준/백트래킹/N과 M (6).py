N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
def recur():
    if len(ans) == M:
        print(*ans)
        return
    for i in arr:
        if len(ans) == 0 or (len(ans) >= 1 and ans[-1] < i):
            ans.append(i)
            recur()
            ans.pop()
recur()