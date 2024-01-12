E, S, M = map(int, input().split())
ans = 1
e_temp = 1
s_temp = 1
m_temp = 1
year = 2
if E == 1 and S == 1 and M == 1:
    ans = 1
else:
    while True:
        e_temp += 1
        s_temp += 1
        m_temp += 1
        if e_temp == 16:
            e_temp = 1
        if s_temp == 29:
            s_temp = 1
        if m_temp == 20:
            m_temp = 1
        year += 1
        if e_temp == E and s_temp == S and m_temp == M:
            break
        ans = year
print(ans)