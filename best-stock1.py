class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_profit = 0
        
        for i in prices:
            
            if i < min_val:
                min_val = i
            
            elif i - min_val > max_profit:
                max_profit = i - min_val
        
        return max_profit
