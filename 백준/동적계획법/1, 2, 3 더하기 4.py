# 다시 또 풀어보기
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]
    
t = int(input())

for _ in range(t):
    N = int(input())
    print(dp[N])


# 5
# 3 2
# 3 1 1
# 2 2 1
# 2 1 1 1 
# 1 1 1 1 1 

# 6
# 3 3
# 3 2 1
# 3 1 1 1
# 2 2 2
# 2 2 1 1
# 2 1 1 1 1
# 1 1 1 1 1 1
