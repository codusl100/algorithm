class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = []
        s = s.lower()
        for i in s:
            if i.isalpha() or i.isdigit():
                alpha.append(i)
        n = len(alpha) - 1
        k = len(alpha) // 2 
        for i in range(k):
            if alpha[i] != alpha[n-i]:
                return False
        return True