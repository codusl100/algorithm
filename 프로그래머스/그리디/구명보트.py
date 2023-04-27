def solution(people, limit):
    people.sort()
    ans = 0
    cnt = 100
    # 50 70 80
    # 50 50 70 80
    while len(people) != 0:
        for i in people:
            if cnt/2 >= i:
                cnt -= i
                people.remove(i)
                if cnt == 0 or cnt < i :
                    ans +=1
            else:
                cnt = 100
                ans += 1
                people.remove(i)
    return ans

print(solution([70,50,80,50], 100))