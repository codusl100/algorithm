t = int(input())
for i in range(t):
    n = int(input())
    p = [0] * (n+1)
    p[1] = 1
    p[2] = 1
    p[3] = 1
    if n > 3:
        for j in range(4, n+1):
            p[j] = p[j-3] + p[j-2]
    print(p[n]) 