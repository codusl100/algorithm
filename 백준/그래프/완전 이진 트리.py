K = int(input())
tree = list(map(int, input().split()))
t_list = [[] for _ in range(K)]

def makeTree(arr, x):
    mid = len(arr) // 2
    t_list[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)

makeTree(tree, 0)

for i in range(K):
    print(*t_list[i])