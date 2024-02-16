N = int(input())
stairs = [int(input()) for i in range(N)]
stairs.reverse()

dp = [0] * N
dp[0] = stairs[0]

for i in range(1, N):
    if i < 3:
        dp[i] = stairs[0] + stairs[i]
    else:    
        dp[i] = max(dp[i-2]+ stairs[i], dp[i-3] + stairs[i-1]+ stairs[i]) 
print(max(dp[N-2], dp[N-1])) 