class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        counter = defaultdict(int)
        maj = len(nums) / 2
        for i in nums:
            counter[i]+=1
            if counter[i] > maj:
                return i
            
