N = int(input())
dp = []

for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i+1):
        # 왼쪽 위 case
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        # 바로 위 case 
        if j == i: 
            up = 0
        else:
            up = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(up_left, up)
    
print(max(dp[N-1]))