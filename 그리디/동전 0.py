# 230114
# 백준 11047번

N, K = map(int, input().split())
B = list()
for i in range(N):
    B.append(int(input()))

B.sort(reverse=True)

count = 0

for b in B :
    count += K // b
    K %= b
        
print(count)

# 진짜 어디가 틀린지 ㅁㄹ겠어서 구글링...
# 리스트 담는 부분을 여러개로 나눠서 (1. 리스트 값 입력받고 2. 이를 int형 리스트로 변환하고 3. reverse해서 주어진 금액보다 작은 금액만 담는 리스트를 다 생성했는데)
# 1, 2번 간소화하고 3 없앴더니 성공 ..;;
# 우선 큰 동전이 전부 작은 동전의 배수가 된다 => 그리디 알고리즘인 것으로 판단