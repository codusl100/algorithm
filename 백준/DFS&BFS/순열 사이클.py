import sys
sys.setrecursionlimit(2000) # 최대 재귀 늘려줌 => 런타임 에러 피할 수 있음

def dfs(x): # DFS 함수 정의
    visited[x] = True # 방문 체크
    number = numbers[x] # 다음 방문 장소
    if not visited[number]: # 방문하지 않았다면
        dfs(number) # 재귀
        
for _ in range(int(input())):
    N = int(input())
    # numbers와 visited 의 0과 True는 각각 0항 의미
    # 1부터 체크하기 때문
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N # 방문 여부 확인용
    result = 0
    
    for i in range(1, N + 1):
        # if 조건문을 추가해서 result 값 중복을 체크할 수 있었어야 했다!
        if not visited[i]: # 방문하지 않았다면
            dfs(i) # DFS 실행
            result += 1 # 결과값 += 1
    print(result)