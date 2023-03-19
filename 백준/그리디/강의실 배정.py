# 230123
# 백준 11000번

N = int(input())

time = []
for i in range(N) :
    a, b = map(int, input().split())
    time.append([a, b])
    
time.sort(key = lambda x : x[0])
time.sort(key = lambda x : x[1])

cnt = 0
end = time[0][1]
for i in range(1, N):
    if time[i][0] >= end:
        end = time[i][1]

print(cnt)