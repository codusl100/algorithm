class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        output = list()

        for i in range(len(candies)):
            output.append((candies[i] + extraCandies) >=maxCandy)


        return output