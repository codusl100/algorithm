K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

ma = max(LAN) 

def binary(mi, ma):      
    while mi <= ma:
        mid = (mi + ma) // 2
        lines = 0
        for i in LAN :
            lines += (i // mid) # lines = 20
        if lines >= N:
            mi = mid + 1
        else:
            ma = mid - 1
    print(ma)


binary(1, ma)