def solution(s):
    ans = len(s)
    N = len(s)
    for step in range(1, N // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step 만큼의 문자열 추출
        cnt = 1
        for j in range(step, N, step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+step] # 다시 상태 초기화
                cnt = 1
        compressed += str(cnt) + prev if cnt >= 2 else prev
        ans = min(ans, len(compressed))
    return ans