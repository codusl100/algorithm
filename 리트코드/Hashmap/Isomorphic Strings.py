class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char = []
        char2 = []
        for i in s:
            char.append(s.index(i))
        for i in t:
            char2.append(t.index(i))
        if char == char2:
            return True
        else:
            return FalseS