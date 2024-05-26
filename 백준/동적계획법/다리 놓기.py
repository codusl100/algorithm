t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    dp = [[1]*(b+1) for _ in range(b+1)]
    for i in range(2, b+1):
        dp[1][i] = i
    
    for i in range(2, a+1):
        for j in range(i+1, b+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp[a][b])