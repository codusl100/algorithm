class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = left + k - 1

        temp = 0
        avg = 0

        for i in range(left, right + 1):
            temp += nums[i]

        avg = temp / k

        while right != len(nums) - 1:
            right += 1
            temp = temp - nums[left] + nums[right]
            left += 1
            avg = max(avg, temp / k)

        return avg