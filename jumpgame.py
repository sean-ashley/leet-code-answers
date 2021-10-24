class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        last_jump = len(nums) - 1
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= last_jump:
                last_jump = i
            
        
        
        
        
        return last_jump == 0
        
