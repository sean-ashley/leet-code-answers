class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        running_sums = []
        for i in nums:
            sums += i
            running_sums.append(sums)
        
        return running_sums
