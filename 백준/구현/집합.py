import sys
input = sys.stdin.readline
check = set()
N = int(input())

for i in range(N):
    temp = input().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            check = set([j for j in range(1, 21)])
        else:
            check = set()
    else:
        str, num = temp[0], int(temp[1])
        if str == 'add':
            check.add(num)
        elif str == 'remove':
            check.discard(num)
        elif str == 'check':
            print(1 if num in check else 0)
        elif str == 'toggle':
            if num in check:
                check.discard(num)
            else:
                check.add(num)