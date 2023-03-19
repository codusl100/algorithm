# 230116
# 백준 1969번

N, M = map(int, input().split())
cnt = 0

A = list(0 for i in range(0,M))
T = list(0 for i in range(0,M))
G = list(0 for i in range(0,M))
C = list(0 for i in range(0,M))

result = list()

for _ in range(N):
    DNA = list()
    DNA = list(input())
    for i in range(0, M):
        if DNA[i] == 'A' :
            A[i] += 1
        elif DNA[i] == 'T' :
            T[i] += 1
        elif DNA[i] == 'G' :
            G[i] += 1
        else:
            C[i] += 1

for i in range(M):
    s_list = list()
    s_list.append(A[i])
    s_list.append(T[i])
    s_list.append(G[i])
    s_list.append(C[i])
    s_list.sort()    
    max_num = max(s_list)
    if max_num == A[i] :
        result.append('A')
        cnt += T[i] + G[i] +C[i]
    elif max_num == C[i] :
        result.append('C')
        cnt += T[i] + G[i] +A[i]
    elif max_num == G[i] :
        result.append('G')
        cnt += T[i] + A[i] +C[i]
    else :
        result.append('T')
        cnt += A[i] + G[i] +C[i]
Result = "".join(result)
print(Result)
print(cnt)

# 동등한 빈도로 출현한 알파벳의 경우 사전순으로 출력해야하는 걸 간과했다! 이 점 고려해서 잘 풀음
# A, C, G, T 수 구할 때 리스트 말고 그냥 정수로 해서 max값 비교해도 됐을듯