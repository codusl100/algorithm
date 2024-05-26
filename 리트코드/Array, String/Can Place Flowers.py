class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            # 현재 항 0 이어야 함
                # 근데 첫번째 항이면 다음 항 0 이어야함
                # 중간 항이면 양 옆 항 다 0 이어야함
                # 마지막 항이면 이전 항 0 이어야 함
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True  
        return False