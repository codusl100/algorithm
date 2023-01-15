# 230116
# 백준 11399번

N = input()
P = list(map(int, input().split()))
P.sort()
# 1 2 3 3 4
new_P = list()

for i in range(1, len(P)+1):
    A = 0
    for j in range(i) :
        A += P[j]
    new_P.append(A)
    
print(sum(new_P))    

# 간단하게 풀었던 문제
# 돈 인출하려면 앞 사람이 인출하는데 걸리는 시간이 더 적어야하므로
# 오름차순으로 정렬해서 같은 값을 더해줬다