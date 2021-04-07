class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        N = len(arr)
        
        i = 0
        
        #walk up
        while i + 1 < N and arr[i] < arr[i+1]:
            i+=1
        
        
        #check if were at the start or the end
        
        if i == 0 or i == N-1:
            return False
        
        while i+1 < N and arr[i] > arr[i+1]:
            i +=1
            
        #see if we made it to the end
        return i == N-1
            
            
        
        
