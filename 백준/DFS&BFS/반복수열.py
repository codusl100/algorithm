A, P = map(int, input().split()) # 57, 2
N = len(str(A)) - 1
B = A
graph = [[]]

# A를 자릿수대로 나눈 후 배열 [5, 7] 생성해서 graph 안에 넣음
print(N)
while N > 0:
    B = A // (10 ** N) # 몫
    graph[0].append(B)
    A %= 10 ** N # 나머지
    N -= 1
graph[0].append(A)

def dfs(v):
    graph[v+1] = []
    for i in range(len(str(A))):
        graph[v+1].append(graph[v][i] ** P)
        
