n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]
ans = [int(1e9)] * n 

for x in coordinates:
    for y in coordinates:
        costs = []
        for ix, iy in coordinates:
            costs.append(abs(x[0] - ix) + abs(y[1] - iy))

        costs.sort()
        cost = 0

        for i in range(n):
            cost += costs[i]
            ans[i] = min(ans[i], cost)

print(*ans)