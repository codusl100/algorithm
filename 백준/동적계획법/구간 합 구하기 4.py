n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
for i in range(m):
    a, b = map(int, input().split())
    dp = [0] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = dp[i-1] + arr[i-1]
    print(dp[b] - dp[a-1])
