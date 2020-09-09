class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in memo:
                return False
            memo.add(n)
        return True
            
            
        
                
        
