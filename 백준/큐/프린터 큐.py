from collections import deque
T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    count = 0

    while q:
        best = max(q)
        front = q.popleft() # q의 제일 앞
        m -= 1

        if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
            count += 1
            if m < 0: # m이 0이면 뽑은 게 나의 숫자라는 뜻
                print(count)
                break
        else:
            q.append(front)
            if m < 0: # 제일 앞에서 뽑히면
                m = len(q) - 1 # 제일 뒤로 이동