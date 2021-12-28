class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #do modified binary search to find smallest val
        
        #can think of it as finding the start of the unrotated array
        
        
        l,r = 0,len(nums) - 1
        
        while l < r:
            
            m = l + (r-l) // 2
            
            #if the midpoint is greater then the right most value, it means 
            #our smallest subarray has to be between those two values
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
            
        
        
        #when this loop ends, our left pointer will be on the minimum value
        start = l
        #lets adjust the right pointer so its on the max value, this value will be one to the left 
        #of our minmum value no matter what
        l = 0
        
        r = len(nums) - 1
        
        
        #if this is true, the target is present in our lower value subarry (that is from the minimum)
        #value to the end
        
        #otherwise , its present in the higher value subarray (that is the right value is our max value)
        if target >= nums[start] and target <= nums[r]:
            l = start
        else:
            r = start -1 
        
        
        while l <= r:
            
            m = l + (r-l) // 2
            
            if nums[m] == target:
                return m
            
            elif nums[m] > target:
                r = m - 1
                
            else:
                l = m + 1
            
            
        return -1
        
        
        
        
