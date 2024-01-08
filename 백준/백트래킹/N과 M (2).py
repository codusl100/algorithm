N, M = map(int, input().split())
ans = []

def back(start):
    if len(ans) == M: # 배열 크기 다 찼는지
        print(" ".join(map(str, ans)))
        return
    for i in range(start, N+1):
        if i not in ans:
            ans.append(i)
            back(i+1) # 재귀
            ans.pop() # return으로 돌아오면 이게 실행

back(1)