while True:
    try:
        n = int(input())
    except:
        break
    num = 1
    cnt = 1
    while True:
        if num % n != 0: # n의 배수가 아니라면
            num = num * 10 + 1
            cnt += 1
        else:
            break
    print(cnt)