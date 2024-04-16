class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        result = {}
        pattern = list(pattern)
        if len(pattern) != len(arr):
            return False
        for i, d in enumerate(pattern):
            if d in result and result[d] != arr[i]:
                return False
            elif d not in result and arr[i] in result.values():
                return False
            elif d not in arr:
                result[d] = arr[i]
        return True
