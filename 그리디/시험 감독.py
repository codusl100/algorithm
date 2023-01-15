# 230115
# 백준 13458번

N = input()
A = list(map(int, input().split()))
B, K = map(int, input().split())

count = int(N)
    
for i in range(len(A)):
    A[i] -= B
    while A[i] > 0 :
        if A[i] < K :
            count += 1
            break
        else :
            count += 1
            A[i] %= K
print(count)