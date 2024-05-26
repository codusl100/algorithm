class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
        array = list(dic.values())
        array.sort()
        right = 0
        for left in range(len(array) - 1):
            right = left + 1
            while right != len(array):
                if array[left] == array[right]:
                    return False
                else:
                    right += 1
        return True