class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = []
        n = len(nums)
        if all(i == 0 for i in nums):
            temp = [0] * n
            return temp
        for i in range(n):
            if nums[i] == 0:
                zero.append(i)
            else:
                total *= nums[i]
        temp = [total] * n
        for i in range(n):
            if len(zero) <= 0: # 0이 하나라도 없다면
                temp[i] = temp[i] // nums[i]
            else: # 0이 하나라도 있으면
                if i not in zero: # 0인 항이라면
                    temp[i] = 0
        return temp
