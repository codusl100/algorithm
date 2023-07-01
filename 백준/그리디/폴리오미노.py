ans = input()
ans = ans.replace("XXXX", "AAAA")
ans = ans.replace("XX", "BB")

if 'X' in ans:
    print(-1)
else :
    print(ans)