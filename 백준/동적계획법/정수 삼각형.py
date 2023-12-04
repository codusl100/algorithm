N = int(input())
dp = []

for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i):
        if j == 0: # 왼쪽 위
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j == i: # 바로 위
            up = 0
        else:
            up = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(up_left, up)
    
print(max(dp[N-1]))