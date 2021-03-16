class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums.sort(key = lambda x : x == val, reverse = True)
        counter = nums.count(val)
        
        i = 0
        while i < counter:
            nums.pop(0)
            i += 1
        return len(nums)
