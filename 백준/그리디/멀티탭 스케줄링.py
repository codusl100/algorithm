# 230123
# 백준 1700번

N, K = map(int, input().split())

item = list(map(int, input().split()))

plug = list()
for i in range(0, N) :
    plug.append(item[i])

cnt = 0
for i in range(N, K) :
    if item[i] not in plug : # 교체해야한다면 
        cnt += 1
        for k in range(i+1, K) :
            if item[k] in plug : # 교체해야할 것 뒤에 plug에 중복되는 것이 있다면
                plug_index = plug.index(item[k])
                plug[plug_index] = item[i]
print(cnt)