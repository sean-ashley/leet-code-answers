class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        #base cases
        if n==1:
            return 1
        elif n == 2:
            return 2
        
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
        return self.memo[n]
        
        
        
