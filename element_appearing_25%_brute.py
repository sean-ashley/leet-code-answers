class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        from collections import defaultdict
        
        numbers = defaultdict(int)
        
        length  = len(arr)
        
        for i in arr:
            
            numbers[i] += 1
            
            
            if numbers[i] / length > 0.25:
                return i
