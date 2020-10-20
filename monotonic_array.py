class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        #check beginning and end of list to see if we
        #should be checking for monotonic increasing or decreasing.
        
        if A[0] <= A[-1]:
            monotonic = 'increasing'
        
        else:
            monotonic = 'decreasing'
            
        
        
        #loop until second last element
        for i in range(len(A)-1):
            #if it is increasing, check if the
            # next element is greater or equal 
            #then the former
            if monotonic == "increasing":
                if not (A[i] <= A[i+1]):
                    return False
            #do same for decreasing
            else:
                if not (A[i] >= A[i+1]):
                    return False
        
        #if we make it thru the loop, it is monotonic
        return True