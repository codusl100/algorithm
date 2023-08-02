N, M = map(int, input().split())
video = [int(i) for i in input().split()]

mi = max(video)
ma = sum(video)
a = 0
while mi <= ma :
    mid = (mi + ma) // 2
    result = []
    for i in video :
        a += i 
        if a > mid :
            result.append(a-i)
            a = i
    result.append(a)
    a = 0
    if len(result) <= M :
        ma = mid - 1
        ans = mid
    else :
        mi = mid + 1
print(ans)