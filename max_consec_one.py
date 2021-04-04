class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        #initialize counts
        curr = 0
        best = 0
        
        for num in nums:
            
            if num == 1:
                curr += 1
            else:
                curr = 0
                
            best = max(curr,best)        
        return best
