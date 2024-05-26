class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums = []
        for i in nums1:
            nums.append(i)
        for i in nums2:
            nums.append(i)
        dic = defaultdict(int)
        first = []
        last = []
        for n in nums:
            dic[n] += 1
        for n1 in nums1:
            if dic[n1] == 1:
                first.append(n1)
        for n2 in nums2:
            if dic[n2] == 1:
                last.append(n2)
        return [first, last]