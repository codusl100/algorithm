# 230114
# 백준 1783번

# 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다. => 그리디 알고리즘
# N M
# 1. +2 +1
# 2. +1 +2
# 3. -1, +2
# 4. -2, +1

# 먼저 오른쪽으로 이동하는 걸 우선으로 고려함
# 이동 횟수가 4 이상인 경우 문제에서 기재된 방법 수 다 적용해야함. -> 오른쪽으로 6은 무조건 움직임
# 그렇기에 이 경우 처음에 가능 이동 오른쪽 범위 M에서 6을 빼주고 남은 M에서 4(문제 조건 필수 방법)를 더해줌


## N = 2일 때 N = 1 일 때처럼 자유롭게 이동 가능한 줄.. => 2, 3번만 쓸 수 있다는 걸 고려 못함
# 이제 오른쪽으로 이동하는 횟수가 6보다 작을 경우가 고민
# 일단 세로의 크기에 따라 오른쪽 가는 것에 영향 받음 
# 우선 세로 가로 1보다 작으면 count는 1임
# 세로가 2라면 2번 3번 방법만 쓸 수 있다
# 3 => 2
# 5 => 3
# 7 => 4
# 규칙성 => M + 1 / 2하면 최대 칸 나옴
# 가로가 6 이하면

N, M = map(int, input().split())

count = 0
# 이동 횟수 4번 미만
if N == 1:
    print(1)
elif N == 2: # 여기가 생각하기 어려웠음
    print(min(4, (M+1)//2)) # 왜 (m+1)//2인지 생각을 못함
    # M이 커짐에 따라 달라진다
elif M <= 6 : # 6이 기준인 건 문제 1, 2, 3, 4 번 다 더했을 때 최소 칸 수가 6이라
    print(min(4, M))
else :
    print(M-2)
    
# 생각보다 코드가 너무 간결했다
# 나올 수 있는 경우의 수들을 추려보며 조건을 나누자!