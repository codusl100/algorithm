N, M = map(int, input().split())
money = [int(input()) for i in range(N)]

m_min = min(money)
m_max = sum(money)

def binary(m_min, m_max):   
    while m_min <= m_max:
        total = 0
        cnt = 1
        mid = (m_min + m_max) // 2
        for i in money:
            if total + i <= mid:
                total += i
            else:
                cnt += 1
                total = i
        if cnt > M or mid < max(money):
            m_min = mid + 1
        else:
            m_max = mid - 1
            k = mid
    return k

print(binary(1, m_max))