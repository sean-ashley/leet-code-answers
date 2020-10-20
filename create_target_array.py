class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        #create_target_array full of zeros
        target_array = []
        
        #loop thru both lists and the same time, creating the target
        # array
        for i,k in zip(nums,index):
            target_array.insert(k,i)
            
        
        
        return target_array