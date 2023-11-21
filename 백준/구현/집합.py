check = set()
N = int(input())
for i in range(N):
    input_ = input().strip().split()
    if len(input_) == 1:
        if input_[0] == 'all':
            check = set([i for _ in range(1, 21)])
        else:
            check = set()
    else:
        str, num = input_[0], input_[1]
        num = int(num)
        if str == 'add' and num not in check:
            check.add(num)
        elif str == 'remove' and num in check:
            check.discard(num)
        elif str == 'check':
            if num in check:
                print(1)
            else:
                print(0)
        elif str == 'toggle':
            if num in check:
                check.discard(num)
            else:
                check.add(num)
    