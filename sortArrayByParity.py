class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        from collections import deque 
        #if the val is odd, just append it to the end
        de = deque()
        #loop thru a copy of a so we dont just loop around forever
        
        for i in A:
            if i % 2:
                de.append(i)
            else:
                de.appendleft(i)
        
        return de
