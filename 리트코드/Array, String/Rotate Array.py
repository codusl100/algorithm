class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        if l == k:
            return
        
        k = k % l
        nums.reverse() 

        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        for i in range(k, (l+k)//2):
            nums[i], nums[l-1-i+k] = nums[l-1-i+k], nums[i]