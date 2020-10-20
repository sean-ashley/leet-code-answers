class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        #declare max indexes and values to compare later in the loop
        max_index = 0
        
        max_value = float('-inf')
        
        #loop thru list
        for i in range(len(arr)):
            
            #if the element is greater then the previous
            # max value, save the new max value and index
            if arr[i] > max_value:
                max_value = arr[i]
                max_index = i
            
        #return the max_index
        return max_index
                
            
        