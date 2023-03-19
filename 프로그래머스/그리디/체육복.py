def solution(n, lost, reserve):
    ans = n - len(lost)
    for i in lost:
        if i+1 in reserve :
            ans += 1
            reserve.remove(i+1)
        elif i-1 in reserve:
            ans += 1
            reserve.remove(i-1)
    return ans