tri = [n*(n+1)//2 for n in range(1, 46)]
result = [0] * 1001

# 미리 유레카 수 구하기
for i in tri :
    for j in tri :
        for k in tri :
            if i + j + k <= 1000 :
                result[i + j + k] = 1

N = int(input())
for i in range(N):
    print(result[int(input())])