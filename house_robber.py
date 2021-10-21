class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge case
        length = len(nums)
        
        
        if length < 3:
            return max(nums)
        
        dp = [nums[0],max([nums[0],nums[1]])]
        
        for i in range(2,length):
            #gives maximum possible shit at i
            dp.append(max(dp[i-2] + nums[i], dp[i-1])) 
        
        
        return dp[-1]
        
        
        
        
        
