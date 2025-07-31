from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0

        for index in range(len(flowerbed)):
            if flowerbed[index] == 0:
                left_is_empty = (index == 0) or (flowerbed[index - 1] == 0)
                right_is_empty = (index == len(flowerbed) - 1) or (flowerbed[index + 1] == 0)
                if left_is_empty and right_is_empty:
                    flowerbed[index] = 1
                    counter += 1
                    if counter >= n:
                        return True

        return counter >= n
