class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow  = nums[slow]
            fast = nums[nums[fast]]
        
            if slow == fast:
                
                break
        
        entry = 0
        
        while True:
            slow = nums[slow]
            entry = nums[entry]
            if slow == entry:
                return slow
                
        
        
        
        
        
