N, M = map(int, input().split())
str = input().split()
tree_list = [int(num) for num in str]

tree_min = min(tree_list) # 4
tree_max = max(tree_list) # 42

def binary(t_min, t_max) :
    while t_min <= t_max :
        mid = (t_min + t_max) // 2 # 23
        n_list = [i-mid if i-mid >= 0 else 0 for i in tree_list]
        if sum(n_list) >= M :
            t_min = mid + 1
        else :
            t_max = mid - 1
    return t_max

print(binary(1, sum(tree_list)))         