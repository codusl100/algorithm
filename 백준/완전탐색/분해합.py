N = int(input())

ans = 0

for i in range(1, N+1):
    num = i + sum(map(int, str(i)))
    if N == num :
        ans = i
        break

print(ans)