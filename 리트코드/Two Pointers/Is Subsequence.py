class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        else:
            left = 0
            l = 0
            right = len(t) - 1
            r = len(s) - 1
            visited_t = [0] * len(t)
            visited_s = [0] * len(s)
            
            while left <= right: 
                if t[left] == s[l] and visited_t[left] == 0:
                    visited_t[left] += 1
                    visited_s[l] += 1
                    l += 1
                if t[right] == s[r] and visited_t[right] == 0:
                    visited_t[right] += 1
                    visited_s[r] += 1
                    r -= 1
                left += 1
                right -= 1
            if any(i == 0 for i in visited_s):
                return False
            else:
                return True