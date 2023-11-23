N, K = map(int, input().split())
temp = []
for i in range(N):
    temp.append(list(map(int, input().split())))
temp.sort(key = lambda x:(x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if temp[i][0] == K:
        index = i

for i in range(N):
    if temp[index][1:] == temp[i][1:]:
        print(i+1)
        break