# 230116
# 모두의 마블

N = input()
level = list(map(int, input().split()))
coin = list()

level.sort(reverse=True)

for i in range(len(level) - 1) :
    coin.append(level[0] + level[i+1])

print(sum(coin))

# 누적된 코인이 갈수록 커지려면, 제일 큰 수와 더해서 값을 불려야한다.
# ATM과 원리가 같다!
# 문제에서 인접한 카드만 합성할 수 있다고 했지만 제일 큰 수와 계속해서 더해나가면 되기에 조건에 얽매이지 않아도 괜찮음