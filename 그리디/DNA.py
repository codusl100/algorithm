# 230116
# 백준 1969번

N, M = map(int, input().split())
DNA = list()
new_DNA = list()

A = list(0 for i in range(0,M))
T = list(0 for i in range(0,M))
G = list(0 for i in range(0,M))
C = list(0 for i in range(0,M))

result = list()
# A = 0
# T = 0
# G = 0
# C = 0
x = list()
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
    x.append(A[i])
    x.append(T[i])
    x.append(G[i])
    x.append(C[i])
    
print(A)
print(T)
print(G)
print(C)
for i in range(M):
    max_num = max(A[i], T[i], G[i], C[i])
    if max_num == A[i] :
        result.append('A')
    elif max_num == T[i] :
        result.append('T')
    elif max_num == G[i] :
        result.append('G')
    else :
        result.append('C')
    print(result)
Result = "".join(result)
print(Result)
