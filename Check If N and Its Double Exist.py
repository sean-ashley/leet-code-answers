class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        nums = set()
        
        for i in arr:
            #if the number x 2 is in there 
            if (i * 2) in nums or ((i /2) in nums and i % 2 == 0):
                return True
            
            #add the number to our list
            nums.add(i)
        return False
