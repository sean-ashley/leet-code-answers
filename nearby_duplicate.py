class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nums_dict = {}
        matches = []
        for i in range(len(nums)):
            
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                matches.append(abs(i - nums_dict[nums[i]])) 
                nums_dict[nums[i]] = i
        if not matches:
            return False
        return True if min(matches) <= k else False
