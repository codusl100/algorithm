class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 길이 다르면 false
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True