class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #ELSE STATEMENT NEEDED INCASE NUMBER APPEARS MORE THEN ONCE, WE DONT WANT TO INCREMENT, CAUSE THEN WE WILL MISS SHIT.
        pointer1=0
        pointer2 =1
        while pointer2 < len(nums):
            
            if nums[pointer1] == nums[pointer2]:
                del nums[pointer1]

            else:
                pointer1 += 1
                pointer2 += 1
        return len(nums)
        
