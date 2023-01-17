# 230117
# 백준 1931번

N = int(input())
arr = list()
for i in range(N) :
    arr.append(list(map(int, input().split())))
arr.sort()

time = list()

start = 0
fin = 0

for i in range(0, N-1) :
    if len(time) == 0 :
        time.append(arr[i])
    # 0항이 기존보다 크고 끝나는 시각 더 적을 때
    start = time[i][0]
    fin = time[i][1]
    else :
        if arr[i][0] == time[-1][0] :
            arr
        if time[-1][1] + (time[-1][1] - time[-1][0]) >= arr[i][0] :
            time.remove(time[-1])
            time.append(arr[i])
    # elif len(time) != 0 :
    #     if time[-1][1] >=
        
print(time)
