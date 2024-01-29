T = int(input())

for i in range(T):
    n, m = map(int, input().split()) # 문서 개수, 몇 번째 인쇄되었는지 궁금한 문서
    arr = [int(i) for i in input().split()]
    ans = 0
    while True:
        now = arr.pop(0)
        if len(arr) == 0:
            ans += 1
            break
        # print(now)
        if now < max(arr):
            arr.append(now)
        else:
            arr.pop()
            ans += 1
            if len(arr) == 0:
                break
        
    print(ans)