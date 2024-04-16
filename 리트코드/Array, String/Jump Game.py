class Solution:
    def canJump(self, nums: List[int]) -> bool:
        limit = nums[0]
        for i, num in enumerate(nums):
            if i > limit:
                return False
            limit = max(limit, i + num)
            if limit >= len(nums) - 1:
                return True
        return True