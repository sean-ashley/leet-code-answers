class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        from collections import deque 
        nums_copy = deque()
        
        #make right and left pointer
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            #if the negative number is greater, put the left number in front 
            if abs(nums[left]) > abs(nums[right]):
                nums_copy.appendleft(nums[left] * nums[left])
                left += 1
            else:
                nums_copy.appendleft(nums[right] * nums[right])
                right -= 1
        
        return nums_copy
