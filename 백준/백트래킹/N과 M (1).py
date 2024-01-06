N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M: # 배열 크기 다 찼는지
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            back() # 재귀
            print("재귀 끝났니")
            ans.pop() # return으로 돌아오면 이게 실행
back()