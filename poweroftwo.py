class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n < 1:
            return False
        elif n== 1:
            return True
        
        return self.isPowerOfTwo(n / 2)
