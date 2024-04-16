class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1
        while idx1 < idx2:
            temp = numbers[idx1] + numbers[idx2]
            if temp == target:
                return [idx1+1, idx2+1]
            if temp < target:
                idx1 += 1
            else:
                idx2 -= 1
            