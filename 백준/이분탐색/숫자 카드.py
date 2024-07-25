N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    s = 0
    e = N - 1
    flag = False
    while s <= e:
        mid = (s + e) // 2
        if arr1[mid] == num:
            flag = True
            break
        elif arr1[mid] > num:
            e = mid - 1
        elif arr1[mid] < num:
            s = mid + 1
    if flag:
        print(1)
    else:
        print(0)