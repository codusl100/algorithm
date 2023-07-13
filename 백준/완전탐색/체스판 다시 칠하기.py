N, M = map(int, input().split())

chess = []
for i in range(N):
    chess.append(input())

cnt = []

for i in range(N-7): # 0, 1, 2
    for j in range(M-7): # 0, ..., 5
        index1 = 0 # 'W'로 시작한 경우 바꿔야할 것
        index2 = 0 # 'B'로 시작한 경우 바꿔야할 것
        for k in range(i, i+8):
            for m in range(j, j+8):
                if (k+m) % 2 == 0: # 행 k + 열 m 값이 짝수면 첫 항과 색이 같아야함
                    if chess[k][m] != 'W': # B이면
                         index1 += 1 # 같아야하는데 다르니까 추가
                    if chess[k][m] != 'B':
                         index2 += 1
                else: # 홀수면 첫 항과 색이 다름
                    if chess[k][m] != 'B':
                         index1 += 1
                    if chess[k][m] != 'W':
                         index2 += 1
        cnt.append(min(index1, index2))
print(min(cnt))