class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:

        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        else:        
            for i, e in enumerate(flowerbed):
                if n == 0:
                    return True

                if e == 0:
                    if (i == 0 and flowerbed[i + 1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0): 
                        flowerbed[i] = 1
                        n -= 1
                    elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    continue
        
        return True if n == 0 else False
                    