from collections import defaultdict
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    race = list(map(int, input().split()))
    cnt = defaultdict(list)
    for i in range(N):
        if race[i] in cnt:
            cnt[race[i]] += 1
        else:
            cnt[race[i]] = 1
    temp = []
    for i in cnt:
        if cnt[i] == 6: # 6명만 출전 O
            temp.append(i)
    result = defaultdict(list)
    k = 1
    for i in range(N):
        if race[i] in temp:
            result[race[i]].append(k)
            k += 1
    min_sum = float('inf')
    min_key = None
    for key in result.keys():
        total = sum(result[key][:4])
        total_5 = result[key][4]
        if total < min_sum or (total == min_sum and total_5 < result[min_key][4]):
            min_sum = total
            min_key = key
    print(min_key)