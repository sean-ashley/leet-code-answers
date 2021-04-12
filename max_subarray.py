class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        currentsub = maxsub = nums[0]
        
        for num in nums[1:]:
            currentsub = max(num,currentsub + num)
            maxsub = max(maxsub,currentsub)
            
        
        return maxsub
        
