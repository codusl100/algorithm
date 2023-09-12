import math
N = int(input())
muscle = list(map(int, input().split()))
muscle = sorted(muscle, reverse=False)
max_muscle = 0
pt = math.ceil(N/2)
i = 0


ans_list = []

if N % 2 != 0: # 홀수
    max_muscle = muscle[N-1]
    while i <= N-i-2:
        ans_list.append(muscle[i]+muscle[N-i-2])
        i += 1
    ans_list.append(max_muscle)
else:
    while i <= N-i-1:
        ans_list.append(muscle[i]+muscle[N-i-1])
        i += 1

print(max(ans_list))
    