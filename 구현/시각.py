# 예제 4-2
N = int(input())
cnt = 0

for i in range(N + 1):
    for k in range(60):
        for m in range(60):
            if '3' in str(i) + str(k) + str(m) :
                cnt += 1
print(cnt)

# 원랜 i, k, m 마다 cnt 더하려고 했는데 그것보다 str값을 다 더해서 3이 있는지 확인하는게 시간 단축 굿