

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        length = len(flowerbed)
        count_ = 0
        for i, flower in enumerate(flowerbed):

            if flower == 0:

                empty_left_plot = (i==0) or (flowerbed[i-1] == 0)

                empty_right_plot = (i==length-1) or (flowerbed[i+1] == 0)

                new_flower = int(empty_left_plot and empty_right_plot)
                count_ += new_flower

                flowerbed[i] = new_flower
        
            if count_ >= n:
                return True 

        return False
