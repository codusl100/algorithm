P = int(input())

for _ in range(P):
    line = list(map(int,input().split()))
    ans = 0
    for i in range(1, len(line)-1):
        for j in range(i+1, len(line)): # i 뒤에 있는 애들과 비교
            if line[i] > line[j]: # i가 더 크면
                line[i], line[j] = line[j], line[i]
                ans += 1
    print(line[0], ans)