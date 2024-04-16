class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        r = numRows - 1
        arr = ['' for i in range(numRows)]
        now = 0
        dir = "up"
        if r == 0:
            return s
        else:
            for i in range(len(s)):
                arr[now] += s[i]
                if now == r:
                    dir = "down"
                elif now == 0:
                    dir = "up"
                if dir == "up":
                    now += 1
                elif dir == "down":
                    now -= 1
            return ''.join(arr)