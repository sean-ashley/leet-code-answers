class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        #base case
        if len(nums) == 1:
            return nums[0]
        dp = range(min(nums),max(nums)+1)
        curr,prev = 0,0
        for i in dp:
            new_curr = max(prev + (i * freq[i]),curr)
            prev = curr
            curr = new_curr
        return curr
            
            
            
        
        
