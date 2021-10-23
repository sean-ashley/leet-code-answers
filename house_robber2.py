class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge case
        length = len(nums)
        
        
        if len(nums) == 1:
            return nums[0]
        #case 1, we are able to rob the first house but not the last
        nums1 = nums[:-1]
        if len(nums1) < 3:
            max1 = max(nums1)
        else:
            dp1 = [nums1[0],max([nums1[0],nums[1]])]
            for i in range(2,len(nums1)):
                #gives maximum possible shit at i
                dp1.append(max(dp1[i-2] + nums1[i], dp1[i-1])) 
            max1 = dp1[-1]
        #case 2 , we cant rob the first house but we can rob the last
        nums2 = nums[1:]
        if len(nums2) < 3:
            max2 = max(nums2)
        else:
            dp2 = [nums2[0],max([nums2[0],nums2[1]])]
            for i in range(2,len(nums2)):
                #gives maximum possible shit at i
                dp2.append(max(dp2[i-2] + nums2[i], dp2[i-1])) 
            max2 = dp2[-1]
        
        
        return max(max1,max2)
        
        
        
        
        
