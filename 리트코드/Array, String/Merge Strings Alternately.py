class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        w1 = 0
        w2 = 0
        t1 = False
        t2 = False
        arr = []
        print(len(word2))
        while t1 != True or t2 != True:
            if w1 != len(word1):
                arr.append(word1[w1])
                w1 += 1
            else:
                t1 = True
            if w2 != len(word2):
                arr.append(word2[w2])
                w2 += 1
            else:
                t2 = True
        return "".join(arr)
