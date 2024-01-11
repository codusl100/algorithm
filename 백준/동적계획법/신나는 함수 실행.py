# dp = [[[1 for _ in range(102)] for _ in range(102)] for _ in range(102)]

# for i in range(0, 101):
#     for j in range(0, 101):
#         for k in range(0, 101):
#             if i <= 50 or j <= 50 or k <= 50:
#                 dp[i][j][k] = 1
#             elif i > 70 or j > 70 or k > 70:
#                 dp[i][j][k] = dp[70][70][70]
#             elif i < j and j < k:
#                 dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
#             else:
#                 dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]
                     
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if(dp[a][b][c] != 0):
        return dp[a][b][c]
    elif a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = "+ str(w(a, b, c)))