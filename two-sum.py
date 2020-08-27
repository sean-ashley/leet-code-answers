class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            goal = target - nums[i] 
            if goal in hash_map:
                return [hash_map[goal],i]
            else:
                hash_map[nums[i]] = i
