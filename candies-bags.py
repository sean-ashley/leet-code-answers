class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_val = max(candies)
        
        bool_list = []
        
        for i in candies:
            if i + extraCandies >= max_val:
                bool_list.append(True)
            else:
                bool_list.append(False)
        
        return bool_list
        
