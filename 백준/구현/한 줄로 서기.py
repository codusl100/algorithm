N = int(input())
diff = list(map(int, input().split()))
people = [0] * N

for i in range(N): # 각 자리에 들어갈 사람 체크
    cnt = 0 
    for j in range(N):
        # 자신의 왼쪽에 키 큰 사람의 수가 맞고 그 자리에 아무도 없다면
        if cnt == diff[i] and people[j] == 0:
            people[j] = i + 1
            break
        # 자리에 아무도 없다면 자신의 왼쪽에 키 큰 사람의 수를 카운트
        elif people[j] == 0:
            cnt += 1

print(*people)