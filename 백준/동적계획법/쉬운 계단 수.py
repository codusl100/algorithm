N = int(input())
dp = [[0 for _ in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1): # 자리수
    for j in range(10): # 0 ~ 9 - 각 숫자의 개수
        if j == 0:
            dp[i][j] = dp[i-1][j+1] # 오른쪽 대각선
        elif j == 9:
            dp[i][j] = dp[i-1][j-1] # 왼쪽 대각선
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] # 오른쪽 + 왼쪽
result = 0
for i in range(10):
    result += dp[N][i]

print(result % 1000000000)