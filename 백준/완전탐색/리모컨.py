# 리모컨에는 버튼 0 ~ 9까지의 숫자, +와 -
N = int(input()) # 이동하려고 하는 채널
M = int(input()) # 고장난 버튼의 개수
buttons = []
if M > 0 :
    buttons = list(map(int, input().split()))
num = 0
# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
min_count = abs(100 - N)

for nums in range(1000001):
    nums = str(nums) 
    for i in range(len(nums)):
        if int(nums[i]) in buttons:
            break
        elif i == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - N) + len(nums))

print(min_count)
