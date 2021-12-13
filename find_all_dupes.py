class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupes = []
        #MAIN IDEA, TRANSLATE LIST TO HASH MAP, CAN BE DONE SINCE EVERY ELEMENT IS
        #WITHIN 1 TO N WHERE N IS LENGTH
        
        #WE WILL KNOW ITS A DUPE, SINCE THE SECOND TIME THE ELEMENT IS VISITED IT WILL BE NEGATIVE
        
        for i in nums:
            #make sure u take abs and subtract 1. abs
            #since its possible we turned it negative (to see if another num was negative) and we still want to be able 
            #to see if that number is a duplicate, and subtract one since the range is 1-indexed
            if nums[abs(i) - 1] < 0:
                dupes.append(abs(i))
            #otherwise, multiply the value at that location by -1, 
            #that way, if anotehr number hashes to there, we know it was already
            #visited, aka a dupe
            else:
                nums[abs(i) - 1] = -1 * nums[abs(i) - 1]
                
        
        return dupes
