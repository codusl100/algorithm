N = int(input())
stairs = []
one_step = 1 # 다 1로 초기화
two_step = 1
for i in range(N):
    stairs.append(int(input()))
stairs[1] = stairs[0] + stairs[1] if N > 0 else 0
stairs[2] = max(stairs[2] + stairs[1], stairs[2]+stairs[0]) if N > 1 else 0
for i in range(3, N):
    if stairs[i-1]+stairs[i] > stairs[i-2]+stairs[i]: # 1칸이 더 크다면
        # 1칸 이동 못하면
        if one_step == 2:
            stairs[i] = stairs[i-2]+stairs[i]
            two_step += 1
            one_step = 1 # 초기화
        else: # 1칸 이동 가능하면
            stairs[i] = stairs[i-1]+stairs[i]
            one_step += 1
    else: # 2칸 이동이 더 크다면
        # 2칸 이동 못하면
        if two_step == 2:
            stairs[i] = stairs[i-1]+stairs[i]
            two_step = 1 # 초기화
            one_step += 1
        else:
            stairs[i] = stairs[i-2]+stairs[i]
            two_step += 1
    print(stairs)
print(stairs[N-1])