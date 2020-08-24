class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
                
        for i in nums:
            if hash_map[i] == 1:
                return i
        
